#! /usr/bin/env python
# -*- coding:utf-8 -*-

class T:
    def __init__(self):
        self.name = "zzz"
    
    def h(self):
        self.age=10

t = T()
t.h()
print t.name, t.age
print '{}'.format(t)

