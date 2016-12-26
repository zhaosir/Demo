#! /usr/bin/env python
# -*- coding:utf-8 -*-

import sys
sys.path.append('gen-py')
 
from helloworld import HelloWorld #引入客户端类
 
from thrift import Thrift 
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def get_client():
    try:

        transport = TSocket.TSocket('localhost', 9090)
        #建立socket
        #选择传输层，这块要和服务端的设置一致
        transport = TTransport.TBufferedTransport(transport)
        #选择传输协议，这个也要和服务端保持一致，否则无法通信
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        #创建客户端
        client = HelloWorld.Client(protocol)
        transport.open()
        return client, transport
    #捕获异常
    except Thrift.TException, ex:
        print "%s" % (ex.message)
    return None, None

def close(transport):
    transport.close()


if __name__ == '__main__':
    import time
    i = 0
    client, transport = get_client()
    if not client or not transport:
        print 'client , transport err'
#        sys.exit(-1)
    while i < 100:
        try:
            print "client - ping"
            print "server - " + client.ping()

            print "client - say"
            msg = client.say("Hello!")
            print "server - " + msg
        except Exception, ex:
            print "call error %s" % (ex.message)
            try:
                transport.open()
            except:
                print 're open error'
        time.sleep(1)
        i+=1

    close(transport)

