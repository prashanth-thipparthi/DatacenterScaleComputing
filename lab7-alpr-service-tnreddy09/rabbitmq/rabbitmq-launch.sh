#!/bin/sh
#
# This is the script you need to provide to launch a rabbitmq instance
# and cause it to run the rabbitmq-install.sh script
#
gcloud beta compute --project=decoded-reducer-258105 instances create rabbitmq --zone=us-central1-a --machine-type=f1-micro --subnet=default --no-address --metadata-from-file startup-script=rabbitmq-install.sh --maintenance-policy=MIGRATE --service-account=473448895014-compute@developer.gserviceaccount.com --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append --tags=default-allow-internal --image=ubuntu-1804-bionic-v20191021 --image-project=ubuntu-os-cloud --boot-disk-size=10GB --boot-disk-type=pd-standard --boot-disk-device-name=instance-2 --reservation-affinity=any
