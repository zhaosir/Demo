#! /usr/bin/env python
# -*- coding:utf-8 -*-

import zmq
import time

port = 8100

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)

while True:
	message = socket.recv()
	print "Received request: ", message
	time.sleep (1)  
	socket.send("World from %s" % port)
