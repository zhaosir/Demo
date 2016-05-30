#! /usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import socket
import time

host = '127.0.0.1'
port = 8500

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    conn = s.connect((host, port))
except Exception, ex:
    print ex
    print sys.exc_info 
s.sendall('hi,%s' % int(time.time()))
data = s.recv(1024)
print data
