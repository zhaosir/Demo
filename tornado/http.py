#! /usr/bin/env python
# -*- coding:utf-8 -*_

from tornado import httpclient
from tornado.httputil import url_concat
from functools import partial
from tornado import gen
import time
import tornado.ioloop

def hadnler_json_request(response,callback=None,exc_message=''):
    url = response.request.url
    print 'reponse from %s' % url

    if response.error:
        response.rethrow()
    else:
        res = response.body
        if callback:
            callback(res)
        return res
        

def _ansy_request(url,method,params,callback=None,exc_message=''):
    http_client = httpclient.AsyncHTTPClient()
    body = None
    if method == 'GET' :
        url = url_concat(url,params)
    else:
        body = params
    print url
    handler_requst = partial(hadnler_json_request,callback=callback,exc_message=exc_message)
    return http_client.fetch(url,
                        method = method,
                        body = body,
                        callback = handler_requst,
                        headers = {})


ansy_request = partial(gen.Task,_ansy_request)



@gen.coroutine
def test():
    ret = yield ansy_request(url='http://127.0.0.1:8500/test',method='GET',params=None)
    print ret

@gen.coroutine
def test1():
    http_client = httpclient.AsyncHTTPClient()
    resp = yield http_client.fetch('http://127.0.0.1:8500/test')
    print resp

@gen.coroutine
def test2():
    http_client = httpclient.AsyncHTTPClient()
    resp = yield gen.Task(http_client.fetch, 'http://127.0.0.1:8500/test')
    raise gen.Return(resp.body)

@gen.coroutine
def test3():
    resp = yield test2()
    print resp
if __name__ == '__main__':
#    test()
    tornado.ioloop.IOLoop.instance().run_sync(test3)
#    time.sleep(2)
