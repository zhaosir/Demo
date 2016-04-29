#! /usr/bin/env python
# -*- coding:utf-8 -*-

class MyTest(object):
    def __new__(self,*args,**kwargs):
        print '__new__'
        return super(MyTest,self).__new__(self,*args,**kwargs)

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
    
    @staticmethod
    def show(msg):
        print 'msg:', msg


if __name__ == '__main__':
    MyTest.hello()

    print '-----'
    t = MyTest('tom')
    getattr(t,'method')
#    t.hello()
#    t.test('add' , **{'a':'v'})

    print '-----'
    MyTest.hello()
    t.hello()
    
