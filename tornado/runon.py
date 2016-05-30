import tornado.ioloop
from tornado.gen import coroutine
from tornado.concurrent import Future
import time

from concurrent.futures import ThreadPoolExecutor
from tornado.concurrent import run_on_executor

class T(object):
    executor = ThreadPoolExecutor(2)

    @run_on_executor
    def test(self, y):
        time.sleep(1)
        return 1 + y
class H(object):
    @staticmethod
    @coroutine
    def add(y):
        t = T()
        ret = yield t.test(y)
        print ret
