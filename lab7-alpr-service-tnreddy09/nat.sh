gcloud compute routers create nat-router --network=default --region=us-central1
gcloud compute routers nats create nat-config --router=nat-router --auto-allocate-nat-external-ips --nat-all-subnet-ip-ranges --enable-logging
