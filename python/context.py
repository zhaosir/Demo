#! /usr/bin/env python
# -*- coding:utf-8 -*-

class ContextT:
    def __init__(self):
        pass
    
    def __enter__(self):
        print 'enter' 

    def __exit__(self, type, value, trace):
        try:
            print type 
            print value
            print trace
            print 'exit'
        except:
            print 'error'


with ContextT():
    a = 1/0
print 'end'
