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
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))  
channel = connection.channel()  
channel.queue_declare(queue = 'hello')  
if len (sys.argv) < 2 :  
    print 'message is empty!'  
    sys.exit(0)  
message = sys.argv[1]  
channel.basic_publish(exchange = '', routing_key='hello', body = message)  
print "[x] sent: '" + message + "'\n"  
connection.close()  
