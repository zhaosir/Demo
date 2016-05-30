import tornado.ioloop
from tornado.gen import coroutine
from tornado.concurrent import Future
import time

from concurrent.futures import ThreadPoolExecutor
from tornado.concurrent import run_on_executor
import runon
from runon import H
import ipdb
#class T:
#    executor = ThreadPoolExecutor(2)
#
#    @run_on_executor
#    def test(self, y):
#        time.sleep(1)
#        return 1 + y
#class H:
#    @staticmethod
#    @coroutine
#    def add(y):
#        t = T()
#        ret = yield t.test(y)
#        print ret

@coroutine
def gt():
#    h = runon.H()
#    yield h.add(1)
    h = getattr(runon, 'H')
    m = getattr(h,'add')
    ret = yield m(2)
    print ret

if __name__ == "__main__":
    tornado.ioloop.IOLoop.instance().run_sync(gt)
