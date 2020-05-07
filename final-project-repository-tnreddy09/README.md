## Welcome to Sniper for Application Security

### Overview
- We provide a Cloud based application security service
- You can protect your servers from Denial of Service attacks by sending the load balancers access logs and application server logs to our cloud service.
- You can also analyse your application logs do detect anomalies using the Kibana Dashboard provided.

### Integration with your application
- Making configuration changes in Nginx.
    - Expose an api which would block the ip address.
    - Add rate limiting in nginx.
    - [Here](https://github.com/rajatbhatnagar94/sniper/blob/master/nginx/webserver.conf) is a sample configuration

- Install Filebeat
    - Install filebeat using the `filebeat/install.sh` - currently works for ubuntu 18.04.

- Monitor logs of application on Kibana [http://34.69.126.246:5601/](http://34.69.126.246:5601/) and enjoy!

