#!/usr/bin/env python

# Re-Uses code from https://github.com/GoogleCloudPlatform/python-docs-samples

import argparse
import os
import time

import googleapiclient.discovery
from six.moves import input
import google.auth
import google.oauth2.service_account as service_account


# [START list_instances]
def list_instances(compute, project, zone):
    result = compute.instances().list(project=project, zone=zone).execute()
    return result['items'] if 'items' in result else None
# [END list_instances]


# [START create_instance]
def create_instance(compute, project, zone, name, bucket):
    # Get the latest Debian Jessie image.
    image_response = compute.images().getFromFamily(
        project='gce-uefi-images', family='ubuntu-1804-lts').execute()
    source_disk_image = image_response['selfLink']

    # Configure the machine
    machine_type = "zones/%s/machineTypes/f1-micro" % zone
    startup_script = open(
        os.path.join(
            os.path.dirname(__file__), 'startup-script2.sh'), 'r').read()
    

    #image_url = "http://storage.googleapis.com/gce-demo-input/photo.jpg"
    #image_caption = "Ready for dessert?"

    config ={
        'name': name,
        'machineType': machine_type,

        # Specify the boot disk and the image to use as a source.
        'disks': [
            {
                'boot': True,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImage': source_disk_image,
                }
            }
        ],

        # Specify a network interface with NAT to access the public
        # internet.
        'networkInterfaces': [{
            'network': 'global/networks/default',
            'accessConfigs': [
                {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
            ]
        }],
        "tags": {
            "fingerprint": "UM91MULCTrQ=",
            "items": [
            "allow-5000",
            "http-server",
            "https-server"
            ]
        },
        # Allow the instance to access cloud storage and logging.
        'serviceAccounts': [{
            "email": "default",
            "scopes": [
                "https://www.googleapis.com/auth/devstorage.read_only",
                "https://www.googleapis.com/auth/logging.write",
                "https://www.googleapis.com/auth/monitoring.write",
                "https://www.googleapis.com/auth/servicecontrol",
                "https://www.googleapis.com/auth/service.management.readonly",
                "https://www.googleapis.com/auth/trace.append"
            ]
        }],

        # Metadata is readable from the instance and allows you to
        # pass configuration from deployment scripts to instances.
        'metadata': {
            'items': [{
                # Startup script is automatically executed by the
                # instance upon startup.
                'key': 'startup-script',
                'value': startup_script
            }, {
                'key': 'bucket',
                'value': bucket
            }]
        }
    }
    return compute.instances().insert(
        project=project,
        zone=zone,
        body=config).execute()
# [END create_instance]


def create_firewall_rule(compute, project, zone, name):

    firewall_body = {
        "allowed": [
            {
            "IPProtocol": "tcp",
            "ports": [
                "5000"
            ]
            }
        ],
        "description": "allow-5000",
        "direction": "INGRESS",
        "disabled": False,
        "enableLogging": False,
        "kind": "compute#firewall",
        "logConfig": {
            "enable": False
        },
        "name": "allow-5000",
        "network": "projects/lab5-255004/global/networks/default",
        "priority": 1000.0,
        "selfLink": "projects/lab5-255004/global/firewalls/allow-5000",
        "sourceRanges": [
            "0.0.0.0/0"
        ],
        "targetTags": [
            "allow-5000"
        ]
    }

    firewall_rule_name = "allow-5000"
    request = compute.firewalls().get(project=project, firewall=firewall_rule_name)
    try:
        # Try if rule exists
        request.execute()
    except:
        # Rule doesn't exist. Create it
        request = compute.firewalls().insert(project=project, body=firewall_body)
        request.execute()

    #request = compute.firewalls().insert(project=project, body=firewall_body)
    #response = request.execute()

# [START wait_for_operation]
def wait_for_operation(compute, project, zone, operation):
    print('Waiting for operation to finish...')
    while True:
        result = compute.zoneOperations().get(
            project=project,
            zone=zone,
            operation=operation).execute()

        if result['status'] == 'DONE':
            print("done.")
            if 'error' in result:
                raise Exception(result['error'])
            return result

        time.sleep(1)
# [END wait_for_operation]

# [START run]
def main(project, bucket, zone, instance_name, wait=True):
    #compute = googleapiclient.discovery.build('compute', 'v1')
    credentials = service_account.Credentials.from_service_account_file(filename='service_account.json')
    compute = googleapiclient.discovery.build('compute', 'v1',credentials=credentials)

    print('Creating Fire wall rule.')
    create_firewall_rule(compute, project, zone, instance_name)
    
    print('Creating instance.')

    operation = create_instance(compute, project, zone, instance_name, bucket)
    wait_for_operation(compute, project, zone, operation['name'])

    instances = list_instances(compute, project, zone)

    print('Instances in project %s and zone %s:' % (project, zone))
    for instance in instances:
        print(instance)
        print(' - ' + instance['name'])
        ip = instance['networkInterfaces'][0]['accessConfigs'][0]['natIP']
        print("""Instance created.It will take a minute or two for the instance to complete work.Check this URL: http://{}:5000""".format(ip))
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('project_id', help='Your Google Cloud project ID.')
    parser.add_argument(
        'bucket_name', help='Your Google Cloud Storage bucket name.')
    parser.add_argument(
        '--zone',
        default='us-west1-b',
        help='Compute Engine zone to deploy to.')
    parser.add_argument(
        '--name', default='demo-instance99', help='New instance name.')

    args = parser.parse_args()

    main(args.project_id, args.bucket_name, args.zone, args.name)
# [END run]
