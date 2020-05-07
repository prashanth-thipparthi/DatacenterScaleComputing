if [ -z "$1" ]
then
        echo "Please enter the name of the app log folder name"
        exit 1
fi
app_log_dir_name=$1
sudo apt update
curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-7.5.0-amd64.deb
sudo dpkg -i filebeat-7.5.0-amd64.deb
sudo filebeat modules enable nginx
sudo sed -i '24s! enabled: false! enabled: true!' /etc/filebeat/filebeat.yml
sudo sed -i "28s!*!$app_log_dir_name/*!" /etc/filebeat/filebeat.yml
sudo sed -i 's/#host:\s"localhost:5601"/host: "34.69.126.246:5601"/' /etc/filebeat/filebeat.yml
sudo sed -i 's/localhost:9200/34.69.126.246:9200/' /etc/filebeat/filebeat.yml
sudo sed -i "31i\ \ fields:" /etc/filebeat/filebeat.yml
sudo sed -i "32i\ \ \ \ appname:\ $app_log_dir_name" /etc/filebeat/filebeat.yml
sudo filebeat setup --dashboards
sudo service filebeat start

