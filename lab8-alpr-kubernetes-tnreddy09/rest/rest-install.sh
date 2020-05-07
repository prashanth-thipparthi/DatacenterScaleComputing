#!/bin/sh
#
# This is the script you need to provide to launch a redis instance
# and cause it to run the redis-install.sh script
#

#mkdir /home/$USER/.ssh || true
# cp /id_rsa /root/.ssh/
# cp /id_rsa.pub /root/.ssh/
# chmod 600 /root/.ssh/id_rsa
# chmod 600 /root/.ssh/id_rsa.pub
# ssh-keyscan github.com >> /root/.ssh/known_hosts
#apt-get update

apt-get install -y python3 python3-pip git

pip3 install flask
pip3 install jsonpickle
pip3 install numpy
pip3 install Pillow
python3 -m pip3 install pika --upgrade
pip3 install redis
pip3 install pika


git clone git@github.com:cu-csci-4253-datacenter-fall-2019/lab8-alpr-kubernetes-tnreddy09.git
sleep 2
cd /lab8-alpr-kubernetes-tnreddy09/rest
ls
pwd
