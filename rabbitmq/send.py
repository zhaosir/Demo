#! /usr/bin/env python
# -*- coding:utf-8 -*-

################
#
#https://github.com/pika/pika
#https://pika.readthedocs.org/en/latest/index.html
# pip install pika
#
##################

import sys
import pika
from pika.credentials import PlainCredentials

host = '192.168.199.232'
port = 5672
user = 'test'
passwd = 'test'
vhost = '/'

credentials = PlainCredentials(username=user, password=passwd)                                                            
parameters = pika.ConnectionParameters(host=host, port=port, virtual_host=vhost, credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()  
channel.queue_declare(queue = 'hello')  
if len (sys.argv) < 2 :  
    print 'message is empty!'  
    sys.exit(0)  
message = sys.argv[1]  
channel.basic_publish(exchange = '', routing_key='hello', body = message)  
print "[x] sent: '" + message + "'\n"  
connection.close()  
