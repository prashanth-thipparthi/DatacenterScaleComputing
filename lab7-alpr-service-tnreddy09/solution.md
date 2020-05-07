### Automatic License Plate Recognition

I followed the below steps to complete the lab7.

### Configuration and Installation of Redis
Installed redis using the given script. 
Configured according the requirement.

### Configuration and Installation of RabbitMQ

Installed rabbitMq with the given script and followed the below tutorial to understand the concepts related to the rabbitMQ https://www.rabbitmq.com/tutorials/tutorial-four-python.html

Installed both redis and rabbitMQ on different instances with external IP disabled.

### REST Server
Rest server is built according to the requirements where it accepts the images and process them according using the worker nodes and stores the processed data in the redis.

PUT: Accept image, calculate md5 hash, store the md5 and image io buffer in the rabbitMQ. Worker nodes process it and stores the final result in the redis databse.

GET: Takes license string and returns file checksums in which the license plate is found. In other GET API, It takes md5 hash and return license plates and latitude, longitude information.

### Workers:

Workers take the data from the queue, processes using Alpr and stores the processed result in the redis.


