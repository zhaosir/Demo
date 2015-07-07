#! /usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.web
import tornado.httpserver
import tornado.ioloop
#import tornado.web.asynchronous
from tornado import gen

import time


class TestAHandler(tornado.web.RequestHandler):
#	@tornado.web.asynchronous
#	@gen.engine
	@gen.coroutine
	def get(self):
#		time.sleep(5)
		yield tornado.gen.Task(tornado.ioloop.IOLoop.instance().add_timeout, time.time() + 5)
		self.write('A')
		self.finish()


class TestBHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('B')


#class Application(tornado.web.Application):
#	def __init__(self):
#		settings = {}
#		tornado.web.Application.__init__(self,handlers=[(r'/a',TestAHandler),(r'/b',TestBHandler)])
#		self.add_handlers(r'.*',(
#			(r'/a','TestAHandler'),
#			(r'/b','TestBHandler')
#		))

if __name__ == "__main__":
#	app = Application()
	app = tornado.web.Application(handlers=[(r'/b',TestBHandler),(r'/a',TestAHandler)])
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(8100)
	tornado.ioloop.IOLoop.instance().start()
