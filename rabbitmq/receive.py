#! /usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import pika
from pika.credentials import PlainCredentials

host = '192.168.199.232'
port = 5672
user = 'u_read'
passwd = 'test'
vhost = '/'

credentials = PlainCredentials(username=user, password=passwd)                                                            
parameters = pika.ConnectionParameters(host=host, port=port, virtual_host=vhost, credentials=credentials)

queue_name = 'test'
try:
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()  
    channel.queue_declare(queue = queue_name )  
except pika.exceptions.ConnectionClosed, closeex:
    print 'closed 1'
    sys.exit(0)
print '[*] Waiting for messages. To exit press CTRL+C'  
   
def callback(ch, method, properties, body):  
     print body  

try:
    channel.basic_consume(callback, queue = queue_name , no_ack = True )  
    channel.start_consuming() 
except pika.exceptions.ConnectionClosed, closeex:
    print 'closed'
print 'bye'

