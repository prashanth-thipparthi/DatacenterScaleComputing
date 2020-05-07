#!/bin/sh
#
# This is the script you need to provide to launch a redis instance
# and cause it to run the redis-install.sh script
#

gcloud beta compute --project=decoded-reducer-258105 instances create worker --zone=us-central1-a --machine-type=n1-standard-8 --subnet=default --no-address --metadata-from-file startup-script=worker-install.sh --maintenance-policy=MIGRATE --service-account=473448895014-compute@developer.gserviceaccount.com --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append --tags=default-allow-internal --image=ubuntu-1604-xenial-v20191024 --image-project=ubuntu-os-cloud --boot-disk-size=10GB --boot-disk-type=pd-standard --boot-disk-device-name=worker --reservation-affinity=any