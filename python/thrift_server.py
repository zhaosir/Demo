#! /usr/bin/env python
# -*- coding:utf-8 -*-


import socket
import sys
sys.path.append('gen-py')
from helloworld import HelloWorld 
from helloworld.ttypes import *
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
class HelloWorldHandler:  
    def ping(self):   
        return "pong"   
    def say(self, msg):
        ret = "Received: " + msg    
        print ret    
        return ret
#创建服务端
handler = HelloWorldHandler()
processor = HelloWorld.Processor(handler)
#监听端口
transport = TSocket.TServerSocket("localhost", 9090)
#选择传输层
tfactory = TTransport.TBufferedTransportFactory()
#选择传输协议
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
#创建服务端 
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory) 
print "Starting thrift server in python..."
server.serve()
print "done!"
