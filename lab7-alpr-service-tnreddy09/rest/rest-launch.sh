#!/bin/sh
#
# This is the script you need to provide to launch a redis instance
# and cause it to run the redis-install.sh script
#
# rest- 18.04 
# worker - 16.04
# redis - 16.04
# rabbitmq - 18.04

gcloud beta compute --project=decoded-reducer-258105 instances create rest-server --zone=us-central1-a --machine-type=f1-micro --subnet=default --network-tier=PREMIUM --metadata-from-file startup-script=rest-install.sh --maintenance-policy=MIGRATE --service-account=473448895014-compute@developer.gserviceaccount.com --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append --tags=default-allow-internal,allow-5000,http-server,https-server --image=ubuntu-1804-bionic-v20191021 --image-project=ubuntu-os-cloud --boot-disk-size=10GB --boot-disk-type=pd-standard --boot-disk-device-name=rest-server1 --reservation-affinity=any