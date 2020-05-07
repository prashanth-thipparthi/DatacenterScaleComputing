#!/bin/sh
#
# This is the script you need to provide to install the rest-server.py and start it running.
# It will be provided to the instance using redis-launch.sh
# #
# gsutil cp gs://dsc_lab7/id_rsa .
# gsutil cp gs://dsc_lab7/id_rsa.pub .
# gsutil cp gs://dsc_lab7/authorized_keys .

# sleep 2

# #mkdir /home/$USER/.ssh || true
# sudo cp /id_rsa /root/.ssh/
# sudo cp /id_rsa.pub /root/.ssh/
# sudo cp /authorized_keys /root/.ssh/

# sudo chmod 600 /root/.ssh/id_rsa
# sudo chmod 600 /root/.ssh/id_rsa.pub
# sudo chmod 600 /root/.ssh/authorized_keys

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

export DEBIAN_FRONTEND=noninteractive 
apt-get install -y openalpr
cd /usr/share/openalpr/runtime_data/ocr/ 
cp tessdata/lus.traineddata .



apt-get install -y python3 python3-pika python3-pillow python3-openalpr python3-redis 

cd /

git clone git@github.com:cu-csci-4253-datacenter-fall-2019/lab8-alpr-kubernetes-tnreddy09.git
sleep 2
cd /lab8-alpr-kubernetes-tnreddy09/worker

#sudo python3 /lab8-alpr-kubernetes-tnreddy09/worker/worker.py &