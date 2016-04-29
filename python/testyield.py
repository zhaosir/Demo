#! /usr/bin/env python
# -*- coding:utf-8 -*-


import ipdb

def getids():
    print 'getids begin'
    yield 1
    print 'getids end'

def do():
#    ipdb.set_trace()
    print 'do begin'
    a = getids()
#    v = a.next()
#    print v
    print 'do end'


if __name__ == '__main__':
    do()
