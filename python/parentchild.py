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
    
    def __call__(self,name):
        print '__call__',name

    @property
    def test_property(self):
        print 'property'

    @classmethod
    def test_classmethod(self):
        print 'classmethod'
        Child.test_staticmethod()

    @staticmethod
    def test_staticmethod():
        print 'staticmechod'

if __name__ == '__main__':
#    Child().bar1('msg')
    Child.test_staticmethod()
    child = Child()
#    child.name = 'jim'
#    print Child().name
#    child('lilei')

    Child.test_classmethod()
    child.test_property
