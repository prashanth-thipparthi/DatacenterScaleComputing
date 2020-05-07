#!/bin/sh
#
# This is the script you need to provide to launch a redis instance
# and cause it to run the redis-install.sh script
#
gsutil cp gs://dsc_lab7/id_rsa .
gsutil cp gs://dsc_lab7/id_rsa.pub .

sleep 2

#mkdir /home/$USER/.ssh || true
sudo cp /id_rsa /root/.ssh/
sudo cp /id_rsa.pub /root/.ssh/
sudo chmod 600 /root/.ssh/id_rsa
sudo chmod 600 /root/.ssh/id_rsa.pub
ssh-keyscan github.com >> /root/.ssh/known_hosts

cd /home/csci2400_anonymous
sudo apt-get update
sleep 2
sudo apt-get install -y python3 python3-pip git


sudo pip3 install flask
sudo pip3 install jsonpickle
sudo pip3 install numpy
sudo pip3 install Pillow
sudo python3 -m pip3 install pika --upgrade
sudo pip3 install redis
sudo pip3 install pika


git clone git@github.com:cu-csci-4253-datacenter-fall-2019/lab7-alpr-service-tnreddy09.git
sleep 2
cd /lab7-alpr-service-tnreddy09/rest
ls
pwd
sudo python3 /home/csci2400_anonymous/lab7-alpr-service-tnreddy09/rest/rest-server.py &