#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Parent(object):
    def __new__(self):
        print 'parent.__new__'
        return super(Parent,self).__new__(self)

    def __init__(self):
        print 'parent.__init__'

    def bar(self,msg):
        print 'parent:',msg

    def hello(self):
        print 'parent.hello'

class Child(Parent):
    def __new__(self):
        name = 'singleon'
        if not hasattr(self,name):
            setattr(self,name,super(Child,self).__new__(self))
        return getattr(self,name)

    def __init__(self):
        print 'child.__init__'
#        super(Child,self).__init__()

    def bar1(self,msg):
        print 'child:',msg
        Parent.bar(self,msg)
        super(Child,self).bar(msg)
        super(Child,self).hello()
    
    def __getattribute__(self,*args,**kwargs):
        print '__getattr__:',args,kwargs
#return object.__getattribute__(self, *args, **kwargs)
        return super(Child,self).__getattribute__(*args,**kwargs)

if __name__ == '__main__':
#    Child().bar1('msg')
    child = Child()
    child.name = 'jim'
    print Child().name
