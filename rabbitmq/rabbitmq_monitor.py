#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
from rabbitmqadmin import main 
from optparse import OptionParser, TitledHelpFormatter
import json

_LOCAL_PATH_ = os.path.abspath(os.path.dirname(__file__))
modules_folder = os.path.abspath(_LOCAL_PATH_ + '/..')
if modules_folder not in sys.path:
    sys.path.append(modules_folder)

fro_folder = os.path.abspath(_LOCAL_PATH_ + '/../..')
if modules_folder not in sys.path:
    sys.path.append(modules_folder)
modules_folder = os.path.abspath(_LOCAL_PATH_ + '/../inc')
if modules_folder not in sys.path:
    sys.path.append(modules_folder)
modules_folder = os.path.abspath(_LOCAL_PATH_ + '/../../lib')
if modules_folder not in sys.path:
    sys.path.append(modules_folder)
modules_folder = os.path.abspath(_LOCAL_PATH_ + '/../../applib')
if modules_folder not in sys.path:
    sys.path.append(modules_folder)
modules_folder = os.path.abspath(_LOCAL_PATH_ + '/../tools')
import ipdb
ipdb.set_trace()
if modules_folder not in sys.path:
    sys.path.append(modules_folder)

#from base import *
from tools.sendmail import *
from lib.formwork import ToolsMixin

from lib.applog import app_log
info, debug, error = app_log.info, app_log.debug, app_log.error


EMAIL_TITLE = 'rabbitmq 报警'
EMAIL_TO = ['zijian.zhao@dianjoy.com']
messagelimit = 100  #队列消息最大数量
rate_ack = 0.7  # 消息处理率 处理数量 / 消息总数

class CustomStdout(object):  
  
    def __init__(self):  
        self.buffer = []  
  
    def write(self, *args, **kwargs):  
        self.buffer.append(args)  
        
    def isatty(self):
        pass

stdout = sys.stdout  

def monitor():
    sys.stdout = CustomStdout()    
    main() 
    _customstd, sys.stdout = sys.stdout, stdout
    if _customstd.buffer and len(_customstd.buffer) > 0:
        vhosts = _customstd.buffer[0]
        try:
            comp(json.loads(vhosts[0]))
        except Exception, ex:
            error('error in monitor:%s', ex) 

def comp(vhosts):
    for vhost in vhosts:
        import ipdb 
        ipdb.set_trace()
        name = vhost.get('name','')
        message = vhost.get('messages', 0)
        messages_ready = vhost.get('messages_ready', 0)
        message_stats = vhost.get('message_stats', None)
        ack = 0
        if message_stats:
            ack = message_stats.get('ack', 0)
        try:
            message = int(message)
            message_body = int(message_body)
            ack = int(ack)
            if message <=0:
                continue
            _rate_ack = ack / message
            info('message:%s  message_body:%s  ack:%s  rate_ack:%s' % (message, message_ready, ack, _rate_ack))
            if message > messagelimit or _rate_ack < rate_ack:
                #waring
                email_content = 'RabbitMq 发生报警。\n message:%s \n message_body:%s \n ack:%s rate_ack:%s \n' % (message, message_ready, ack, _rate_ack)
                send_mail(MAIL_CONFIG['smtp_server'], MAIL_CONFIG['smtp_port'], MAIL_CONFIG['user'], MAIL_CONFIG['pwd'], MAIL_CONFIG['user'], EMAIL_TO, [], EMAIL_TITLE, email_content, [])
        except Exception, ex:
            error('error comp:%s', ex)


if __name__ == '__main__':
#python rabbitmq_monitor.py -H 192.168.199.232 -u admin -p admin --format=raw_json list vhosts
    monitor()
