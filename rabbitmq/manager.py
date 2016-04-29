#!/usr/bin/env python  
# -*- coding: utf-8 -*-  

import pika
import sys
from pika.credentials import PlainCredentials

credentials = PlainCredentials(username='test', password='test')
parameters = pika.ConnectionParameters(host = '192.168.199.232', port=5672, credentials=credentials )
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue = 'task_queue_test' , durable = True )
message = ' ' .join(sys.argv[ 1 :]) or "Hello World!"
channel.basic_publish(exchange = '',
                       routing_key = 'task_queue' ,
                       body = message,
                       properties = pika.BasicProperties(
                          delivery_mode = 2 , # make message persistent
                       ))
print " [x] Sent %r" % (message,)
connection.close()
