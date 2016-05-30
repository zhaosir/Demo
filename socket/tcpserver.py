#! /usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import thread

host = '127.0.0.1'
port = 8500

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'fileno:%s' % s.fileno()
try:
    s.bind((host, port))
    print 'fileno:%s' % s.fileno()
except Exception, ex:
    print ex

def clientthread(conn, addr):
    print 'client fileno:%s' % conn.fileno()
    while 1:
        data = conn.recv(1024)
        print 'recv:%s' % data
        if data == 'exit':
            conn.close()
            break
        conn.sendall('ok' + data)


s.listen(1)
while 1:
    print 'wait...'
    conn, addr = s.accept()
    print 'connection with:%s:%s' % (addr[0], addr[1])
    thread.start_new_thread(clientthread, (conn, addr))
s.close()
