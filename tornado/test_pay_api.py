#! /usr/bin/env python
# -*- coding:utf-8 -×-


import unittest
#from unittest.mock import Mock
from tornado.testing import AsyncTestCase, AsyncHTTPTestCase
from tornado.testing import gen_test
from basetest import basetest
from tornado import gen
from tornado import httpclient
import tornado.ioloop
import json

@gen.coroutine
def fetch_url():
    url = 'http://127.0.0.1:8500/test'
    print 'fetch:', url
    http_client = httpclient.AsyncHTTPClient()
    resp = yield http_client.fetch(url)
    raise gen.Return(resp.body)

class PayLibTestCase:#(basetest):

    def setUp(self):
        pass
#        self.wx_pay = WXPayManager
#        self.ali_pay = AliPayManager()
    
    def tearDown(self):
        pass

    @gen.coroutine
    def get_order(self):
        resp = yield fetch_url()
        print resp

 
    @gen.coroutine
    def test_wx_order_query(self):
        transaction_id, out_trade_no = '1008400585201601202797251387', '' #'1008450740201411110005820873', '12345678'
#        print json.dumps(order_info)

    @gen.coroutine
    def test_ali_order_query(self):
        out_trade_no, trade_no = '2016032421001004090286948396', ''


@gen.coroutine
def run():
#    unittest.main()
#    yield test_case.test_wx_order_query()



class TornadoTestCase(AsyncTestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @gen_test
    def test_t(self):
        response = yield self.fetch('http://127.0.0.1/test')
        print response.body
        self.assertEqual(response.code, 200)

if __name__ == '__main__':
    unittest.main()
#    tornado.ioloop.IOLoop.current().run_sync(run)
#    def final_run():
#        unittest.main()
#    tornado.ioloop.IOLoop.current().run_sync(run)
