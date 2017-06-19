#/usr/bin/env python
#-*- coding:utf-8 -*-


import sys
import functools
from functools import partial
from functools import update_wrapper
from functools import reduce
#from test import MyTest
test = __import__('test')

t = {
    'info' : {
        'first' : 'zhang',
        'last' : 'lin',
        'age' : 16,
        'address' : {
            'p' : 'bj',
            'zcode' : 10010
        }
    },
    'email' : 'abc@123',
    'no' : 134
}

def test(a):
    for v in a.itervalues():
        if isinstance(v,dict):
            for i in test(v):
                yield i
        elif isinstance(v,str):
            yield v



def add(a,b):
    return a + b


def wrapper_a(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print args
        return func(*args,**kwargs) + ' word !'
    return wrapper

@wrapper_a
def test_warpper():
    '''this is test_warpper
    '''
    return 'hello'


class MRange(object):
    def __init__(self,count):
        self.count = count
        self.cur = 0

    def next(self):
        while self.cur < self.count:
            yield self.cur
            self.cur = self.cur + 1


@wrapper_a
class testC:
    def __init__(self):
        print "__init__"

if __name__ == '__main__':
    t = testC()
#    a = test(t)
#    print a.next()
#    if hasattr(test, 'MyTest'):
#        print 'xxx'
#    m = MyTest('jim')
#    m.test()
#    for i in MRange(10).next():
#        print i

#    print filter(lambda x : x!='a','iahaha')
#    print map(lambda x,y : x - y ,(1,2),(3,4))
#    print reduce(lambda x,y:x+y,xrange(100))  
    
#    add1 = partial(add,b=1)
#    print add1(2)

#    print test_warpper.__doc__
#    for a in test(t):
#        print a
