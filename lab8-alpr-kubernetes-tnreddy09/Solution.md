### Automatic License Plate Recognition

I followed the below steps to complete the lab8.

### Creation of Docker files
Created a DOcker file for redis 
Created a DOcker file for kubernetes
Created a DOcker file for rest server
Created a DOcker file for worker

### Creation of  Deployment.yaml file

Created a deployment.yaml file for redis 
Created a deployment.yaml file for kubernetes
Created a deployment.yaml file for rest server
Created a deployment.yaml file for worker

### Creation of  Deployment-service.yaml file

Created a deployment.yaml file for redis 
Created a deployment.yaml file for kubernetes
Created a deployment.yaml file for rest server

### REST Server
Rest server is built according to the requirements where it accepts the images and process them according using the worker nodes and stores the processed data in the redis.

PUT: Accept image, calculate md5 hash, store the md5 and image io buffer in the rabbitMQ. Worker nodes process it and stores the final result in the redis databse.

GET: Takes license string and returns file checksums in which the license plate is found. In other GET API, It takes md5 hash and return license plates and latitude, longitude information.

### Workers:

Workers take the data from the queue, processes using Alpr and stores the processed result in the redis.


