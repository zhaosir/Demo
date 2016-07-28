#! /usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.gen
from raven.contrib.tornado import AsyncSentryClient
from raven.contrib.tornado import SentryMixin

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class UncaughtExceptionExampleHandler(
        SentryMixin, tornado.web.RequestHandler):
    def get(self):
        1/0

class AsyncExampleHandler(SentryMixin, tornado.web.RequestHandler):
    def get(self):
        self.write("You requested the main page")
        self.captureMessage("Request for main page served")

class AsyncMessageHandler(SentryMixin, tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        self.write("You requested the main page")
        yield tornado.gen.Task(
            self.captureMessage, "Request for main page served"
        )
        self.finish()

class AsyncExceptionHandler(SentryMixin, tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        try:
            raise ValueError()
        except Exception as e:
            response = yield tornado.gen.Task(
                self.captureException, exc_info=True
            )
        self.finish()

application = tornado.web.Application([
    (r"/", MainHandler),
	(r"/ex", UncaughtExceptionExampleHandler),
	(r"/asyn_ex", AsyncExampleHandler),
	(r"/asyn_msg", AsyncMessageHandler),
	(r"/asyn_ex_1", AsyncExceptionHandler)
])

application.sentry_client = AsyncSentryClient(
    'http://5d6bc055b3b54e2da9b9a338373adc3d:a1419f77ffaf4a57a455953418605e02@sentry.dev.pdt5.medlinker.net/2'
#    'http://e8991445a05348b0990d30cae92f31d2:29cdcd989c034fa8a80dd7e24668d286@sentry.demo.com/2'
)


if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.bind(8500)
    http_server.start()
    tornado.ioloop.IOLoop.instance().start()
