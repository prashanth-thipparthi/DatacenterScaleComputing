#!/usr/bin/env python

import argparse
import os
import time

import googleapiclient.discovery
from six.moves import input
from pprint import pprint

# [START list_instances]
def list_instances(compute, project, zone):
    result = compute.instances().list(project=project, zone=zone).execute()
    return result['items'] if 'items' in result else None
# [END list_instances]


# [START create_instance]
def create_instance(compute, project, zone, name, snapshot_name, bucket):
    # Get the latest Debian Jessie image.
    image_response = compute.images().getFromFamily(
        project='gce-uefi-images', family='ubuntu-1804-lts').execute()
    source_snapshot = "projects/%s/global/snapshots/%s"%(project,snapshot_name)

    # Configure the machine
    machine_type = "zones/%s/machineTypes/f1-micro" % zone
    startup_script = open(
        os.path.join(
            os.path.dirname(__file__), 'startup-script.sh'), 'r').read()
    

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
                    'sourceSnapshot': source_snapshot,
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

def create_snapshot(compute, project, zone, name, snapsot_devicename):
    #source_disk_image = "projects/%s/zones/%s/disks/%s"%(project,zone,snapsot_devicename)
    disk_body = {
        "name": name
    }

    return compute.disks().createSnapshot(project=project, zone=zone,disk= snapsot_devicename, body=disk_body).execute()
    #response = request.execute()
    #pprint(response)

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

def write_timigs(snapshot_times):
    if len(snapshot_times) == 3:
        t1 = str(snapshot_times[0])
        t2 = str(snapshot_times[1])
        t3 = str(snapshot_times[2])

        file_name = "timings.txt"
        open(file_name,'w').close()
        time_string = """snapshot-1: {} , snapshot-2: {}, snapshot-3: {}""".format(t1,t2,t3)
        with open(file_name,'w') as f:
            f.write(time_string)
    else:
        print("Snapshots didn't get created properly")	

# [START run]
def main(project, bucket, zone, wait=True):
    compute = googleapiclient.discovery.build('compute', 'v1')
    
    instances = list_instances(compute, project, zone)

    print('Instances in project %s and zone %s:' % (project, zone))
    for instance in instances:
        print(' - ' + instance['name'])
        inst_name = instance['name']
        snapshot_name = "base-snapshot-"+inst_name
        operation1 = create_snapshot(compute,project, zone,snapshot_name,inst_name)
        wait_for_operation(compute, project, zone, operation1['name'])
        
        snapshot_times = []
        for i in range(3):
            start_time = time.time()
            operation = create_instance(compute, project, zone, "snapshot"+str(i), snapshot_name,bucket)
            wait_for_operation(compute, project, zone, operation['name'])
            duration = time.time() - start_time
            snapshot_times.append(duration)
        
        write_timigs(snapshot_times)
    


    '''
    print('Taking snapshot.')
    operation = create_snapshot(compute, project, zone, instance_name, snapshot_instance_name, bucket)
    #wait_for_operation(compute, project, zone, operation['name'])
    #time.sleep(5)
    operation = create_instance(compute, project, zone, instance_name,snapshot_instance_name, bucket)
    wait_for_operation(compute, project, zone, operation['name'])    

    print("""Instance created.It will take a minute or two for the instance to complete work.Check this URL: http://{}:5000

    Once the image is uploaded press enter to delete the instance.""".format(bucket))
    '''

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
        '--name', default='demo-instance1', help='New instance name.')

    args = parser.parse_args()

    main(args.project_id, args.bucket_name, args.zone)
# [END run]ct, zone=zone, body=disk_body)
