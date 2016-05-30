#! /usr/bin/env python
# -*- coding:utf-8 -*-

class MyTest(object):
#    def __new__(self,*args,**kwargs):
#        print '__new__'
#        return super(MyTest,self).__new__(self,*args,**kwargs)

    def __init__(self,name):
        print '__init__'
        self.name = name

    def test(self, add, **kwargs):
        print 'test' ,self.name
        print add
        print kwargs

    @classmethod
    def hello(self):
        if not hasattr(self,'name'):
            print 'hello'
        else:
            print 'hello' ,self.name
            
    def tip(cls):
        print 'tip'

    def show(self):
        print 'method in show' 

    def config(self):
        return dict()

class Test1(object):
   def __new__(cls, *args, **kwargs):
#        base = cls.config()
#        if cls is base:
#            impl = base.config() 
#        else:
#            impl = base 
#        cls.config()
        instance = super(Test1, cls).__new__(Test3)
        return instance

class Test2(Test1):
    pass

class Test3(Test2):
#    def __new__(cls, *args, **kwargs):
#        base = cls.config()
#        if cls is base:
#            impl = base.config() 
#        else:
#            impl = base 
#        cls.config()
#        instance = super(Test2, cls).__new__(MyTest)
#        return instance

    def tip(self):
        print 'test3.tip'

    @classmethod
    def config(cls):
        print cls
        print 'config'
#        return MyTest('jim')

if __name__ == '__main__':
    a = Test2()
    print a.tip()
#    MyTest.show('f')
    
