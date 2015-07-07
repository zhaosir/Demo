#! /usr/bin/env python
# -*- coding:utf-8 -*-

import zmq
import sys

port = "8100"

context = zmq.Context()
print "Connecting to server..."
socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:%s" % port)
for request in range (1,10):
	print "Sending request ", request,"..."
	socket.send ("Hello")
	message = socket.recv()
	print "Received reply ", request, "[", message, "]"
