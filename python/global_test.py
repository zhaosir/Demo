#! /usr/bin/env python
# -*- coding:utf-8 -*-

i = 1

def p():
    global i
    i += 1
    print i


class T(object):
    def add(self):
        global i
        print i
        i += 1
        print i
p()
