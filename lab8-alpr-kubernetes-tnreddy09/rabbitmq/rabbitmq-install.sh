#!/bin/sh
#
# This is the script you need to provide to install rabbitmq and start it running.
# It will be provided to the instance using rabbitmq-launch.sh
#


export DEBIAN_FRONTEND=NONINTERACTIVE
echo "deb http://www.rabbitmq.com/debian/ testing main"  | sudo tee  /etc/apt/sources.list.d/rabbitmq.list > /dev/null
wget https://www.rabbitmq.com/rabbitmq-signing-key-public.asc
sudo apt-key add rabbitmq-signing-key-public.asc
sudo apt-get update

sudo apt-get install rabbitmq-server -y
sudo bash -c echo "loopback_users=none" >> /etc/rabbitmq/rabbitmq.conf
sudo rabbitmqctl add_user test test
sudo rabbitmqctl set_user_tags test administrator
sudo rabbitmqctl set_permissions -p / test ".*" ".*" ".*"
sudo systemctl restart rabbitmq-server