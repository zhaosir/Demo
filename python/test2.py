#! /usr/bin/env python
# -*- coding:utf-8 -*-

import functools
import sys

debug_log = sys.stderr

def trace(func):
  if debug_log:
    @functools.wraps(func)
    def callf(*args, **kwargs):
      """A wrapper function."""
      debug_log.write('Calling function: {}\n'.format(func.__name__))
      res = func(*args, **kwargs)
      debug_log.write('Return value: {}\n'.format(res))
      return res
    return callf
  else:
    return func

@trace
def square(x):
  """Calculate the square of the given number."""
  return x * x


def subway():
    price = 8
    total_day = 22
    p_10 = 0
    p_8 = 0
    p_5 = 0
    c_cost = 0.0
    for d in xrange(total_day):
        _price = price
        if c_cost >= 100 and c_cost < 150:
            _price = price * 0.8
            p_8 += 1
        elif c_cost >= 150 and c_cost < 200:
            _price = price * 0.5
            p_5 += 1
        else:
            p_10 += 1

        c_cost += _price
    return (c_cost, p_10, p_8, p_5)


class Test:
    @staticmethod
    def check():
        return True

    @staticmethod
    def user(func):
        def wrapper(*args, **kwargs):
            print 'in Test.userWrapper'
            print Test.check()
            func(*args, **kwargs)
        return wrapper

@Test.user
def testwrapper():
    print 'in method testwrapper'

if __name__ == '__main__':
    testwrapper()
#    print subway()
#  print(square(3))
#  print '-' * 30
#  print(square.__doc__)
#  print(square.__name__)
