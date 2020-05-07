#!/bin/bash
gsutil cp gs://dsc_lab5/id_rsa .
gsutil cp gs://dsc_lab5/id_rsa.pub .

sleep 15

#mkdir /home/$USER/.ssh || true
sudo cp /id_rsa /root/.ssh/
sudo cp /id_rsa.pub /root/.ssh/
sudo chmod 600 /root/.ssh/id_rsa
sudo chmod 600 /root/.ssh/id_rsa.pub
ssh-keyscan github.com >> /root/.ssh/known_hosts

cd /home/$USER
sudo apt-get update
sleep 2
sudo apt-get install -y python3 python3-pip git
sleep 2
sudo pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
sleep 2
git clone git@github.com:cu-csci-4253-datacenter-fall-2019/lab5-programmable-cloud-tnreddy09.git
sleep 2
cd /home/$USER/lab5-programmable-cloud-tnreddy09/part3
gsutil cp gs://dsc_lab5/service_account.json .
sudo python3 stage2.py lab5-255004 dsc_lab5