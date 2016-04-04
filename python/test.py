#! /usr/bin/env python
# -*- coding:utf-8 -*-

class MyTest(object):
    def __new__(self,*args,**kwargs):
        print '__new__'
        return super(MyTest,self).__new__(self,*args,**kwargs)

    def __init__(self,name):
        print '__init__'
        self.name = name

    def test(self):
        print 'test' ,self.name

    @classmethod
    def hello(self):
        if not hasattr(self,'name'):
            print 'hello'
        else:
            print 'hello' ,self.name



if __name__ == '__main__':
    MyTest.hello()

    print '-----'
    t = MyTest('tom')
    t.hello()
    t.test()

    print '-----'
    MyTest.hello()
    t.hello()
    
