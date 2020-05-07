##
## Sample Flask REST server implementing two methods
##
## Endpoint /api/image is a POST method taking a body containing an image
## It returns a JSON document providing the 'width' and 'height' of the
## image that was provided. The Python Image Library (pillow) is used to
## proce#ss the image
##
## Endpoint /api/add/X/Y is a post or get method returns a JSON body
## containing the sum of 'X' and 'Y'. The body of the request is ignored
##
##
import hashlib
from flask import Flask, request, Response
import jsonpickle
import numpy as np
from PIL import Image
import io
import pika
import json

# RabbitMQ new task
import pika
import sys

#redis
import redis

credentials = pika.PlainCredentials('test', 'test')
parameters = pika.ConnectionParameters('rabbitmq', 5672,'/',credentials)
connection = pika.BlockingConnection(parameters=parameters)
channel = connection.channel()
channel.exchange_declare(exchange = 'logger', exchange_type = 'topic')
channel.exchange_declare(exchange = 'toWorker', exchange_type = 'direct')
   
channel.queue_declare(queue='workqueue', durable=True)
channel.queue_declare(queue='logger')
# print(" [x] Sent %r" % message)

redisClient1 = redis.StrictRedis(host='redisvm', port=6379, db=1,charset="utf-8", decode_responses=True)
redisClient2 = redis.StrictRedis(host='redisvm', port=6379, db=2,charset="utf-8", decode_responses=True)
redisClient3 = redis.StrictRedis(host='redisvm', port=6379, db=3,charset="utf-8", decode_responses=True)

def add_to_redis(db,key,value):
    if db == 1:
        redisClient1.sadd(key,value)    
    elif db == 2:
        redisClient2.sadd(key,value)   
    elif db == 3:
        redisClient3.sadd(key,value)

# Initialize the Flask application
app = Flask(__name__)
# route http posts to this method
@app.route('/image/<filename>', methods=['PUT'])
def computeMD5(filename):
    r = request
    # convert the data to a PIL image type so we can extract dimensions
    #try:
    ioBuffer = io.BytesIO(r.data)
    img = Image.open(ioBuffer)
    m = hashlib.md5(img.tobytes())
    hashval = m.hexdigest()
    redis_db1_rec = {filename : hashval}
    rabbit_message = {hashval : jsonpickle.encode(ioBuffer)}
    add_to_redis(1,filename,hashval)
    #except:
     #   response = { 'MD5sum' : 0}
        #rabbit_message = {hash:img}
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(redis_db1_rec)
    rabbit_message_pickled = jsonpickle.encode(rabbit_message)
        
    channel.basic_publish(
            exchange='toWorker',
            routing_key='toWorker',
            body=json.dumps(rabbit_message_pickled),
            properties=pika.BasicProperties(delivery_mode=2,  # make message persistent
         ))
    message1 = "Image and hash are placed in the worker queue "
    channel.basic_publish(
            exchange='logger',
            routing_key='info',
            body=json.dumps(message1),
            properties=pika.BasicProperties(delivery_mode=2,  # make message persistent
         ))
    channel.basic_publish(
           exchange='logger',
           routing_key='info',
           body=json.dumps('response from server: '),
           properties=pika.BasicProperties(delivery_mode=2,  # make message persistent
        ))
    #return
    #except Exception as e :
    #    print(e)
    return Response(response=response_pickled, status=200, mimetype="application/json")

@app.route('/hash/<checksum>', methods=['GET'])
def licenseplates_by_checksum(checksum):
    license_plates = [] 
    geo_info = []
    for x in redisClient2.smembers(checksum):
         y = str(x)
         arr = y.split(':')
         license_plates.append(str(arr[0]))
         if(len(arr) > 3):
            lat_long = str(arr[2]) + ":" + str(arr[3])
            geo_info.append(lat_long)
    response = {"license_plates" : license_plates,
                "lat_long": geo_info }
    
    response_pickled = jsonpickle.encode(response)
    message2 ="Logs get checksum"
    channel.basic_publish(
            exchange='logger',
            routing_key='info',
            body=json.dumps('In get by checksum response from server: '),
            properties=pika.BasicProperties(delivery_mode=2,  # make message persistent
         ))
    return Response(response=response_pickled, status=200, mimetype="application/json")
  
@app.route('/license/<license>', methods=['GET'])
def checksum_by_licenseplates(license):
    checksums = []
    for x in redisClient3.smembers(license):
         y = str(x)
         checksums.append(y)
    response = {"license_plate" : license,
                "checksum": checksums }

    response_pickled = jsonpickle.encode(response)
    message3 ="Logs get license"
    channel.basic_publish(
            exchange='logger',
            routing_key='info',
            body=json.dumps('In get licenseresponse from server: '),
            properties=pika.BasicProperties(delivery_mode=2,  # make message persistent
         ))

    return Response(response=response_pickled, status=200, mimetype="application/json")
# start flask app
app.run(host="0.0.0.0", port=5000)