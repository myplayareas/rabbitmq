#!/usr/bin/env python
import pika
 
rabbitmq_broker_host = '192.168.0.8'

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()
 
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
     print(" [x] Received %r" % body)
 

channel.basic_consume('hello', callback, auto_ack=True)
 
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
