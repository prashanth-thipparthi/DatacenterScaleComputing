import getLatLon
import getAlpr
import pika
import time
import json
from PIL import Image
import re
import jsonpickle
import redis

redisClient2 = redis.StrictRedis(host='redisvm', port=6379, db=2)
redisClient3 = redis.StrictRedis(host='redisvm', port=6379, db=3)


def add_to_redis(db,key,value):
    if db == 2:
        redisClient2.sadd(key,value)
    elif db == 3:
        redisClient3.sadd(key,value)

credentials = pika.PlainCredentials('test', 'test')
parameters = pika.ConnectionParameters('rabbitmq', 5672,'/',credentials)
connection = pika.BlockingConnection(parameters=parameters)
channel = connection.channel()
channel.exchange_declare(exchange='logger', exchange_type='topic')
channel.exchange_declare(exchange='toWorker', exchange_type='direct')

logs = channel.queue_declare('logger')
logs_queue = logs.method.queue

worker = channel.queue_declare('workqueue',durable =True)
worker_queue = worker.method.queue

channel.queue_bind(exchange='logger', queue=logs_queue, routing_key='debug')
channel.queue_bind(exchange='logger', queue=logs_queue, routing_key='info')

channel.queue_bind(exchange='toWorker', queue=worker_queue, routing_key='toWorker')

def callback(ch, method, properties, body):
    # print(" [x] Received message")
    print("here1")
    values = body.decode('utf-8')
    values =jsonpickle.decode(values)
    xx = json.loads(values)
    # print()
    for key, value in xx.items():
        ioBytesval = jsonpickle.decode(value) 
        image = Image.open(ioBytesval)
        image.save("/tmp/image.jpg")
        exif_data = getLatLon.get_exif_data(image)
        print(exif_data)
        lat_long = getLatLon.get_lat_lon(exif_data)
        print(lat_long)
        if None not in lat_long:
            #print ("Get lat long",getLatLon.get_lat_lon(exif_data))
            print("here1")

            results = getAlpr.getplate('/tmp/image.jpg')
            print(results)
            # key ="license:confidence:lat:lon"
            if(len(results['results']) > 0):
                plate = str(results['results'][0]['plate'])
                confidence = str(results['results'][0]['confidence'])
                print(plate, confidence)
                value1 = plate + ":" + confidence +":"+str(lat_long[0])+":"+str(lat_long[1])
                add_to_redis(2,key,value1) 
                add_to_redis(3,plate,key) 
            #print("Get plate info",results['results'])

    
    ch.basic_ack(delivery_tag=method.delivery_tag)

def logs_callback(ch, method, properties, body):
    print('logs'," Routing key: ",method.routing_key," Body: ",body)

channel.basic_consume(queue=worker_queue, on_message_callback=callback)
channel.basic_consume(queue=logs_queue, on_message_callback=logs_callback)
channel.start_consuming()
