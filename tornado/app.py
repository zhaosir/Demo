#! /usr/bin/env python
# -*- coding : utf-8 -*-

import tornado
import tornado.web
import time
import tornado.httpserver
import tornado.ioloop
from tornado.options import define,options
import logging


logger = logging.getLogger(__name__)

class Tools(object):

    def __init__(self):
        self.count = 0
        print 'Tools.__init__'

class testHandler(tornado.web.RequestHandler, Tools):

    def initialize(self):
        if hasattr(self,'num'):
            print self.num
        self.num = 0

        if hasattr(self,'num'):
            print 'alter:',self.num
        print 'testHandler.initialize'
#
#    def __init__(self, *args, **kwargs):
#        print 'testHandler.__init__'

    def get(self):
        self.count += 1
        self.num += 1
        logger.debug('debug:%s',time.time())
        self.write({
                    'code' : 1,
                    'time' : int(time.time()),
                    'count' : self.count,
                    'num' : self.num
                })


    def post(self):
        self.get()

host = '.*'
urls = [
    (r'/test','app.testHandler')
]

class App(tornado.web.Application):
    def __init__(self):
        setting = {
            'debug' : options.debug,
            'gzip' : True
        }

        tornado.web.Application.__init__(self,**setting)
        self.add_handlers(host,urls)
        

if __name__ == '__main__':
    define('port',default=8500)
    define('debug',default=False)
    define('t',default=1)
    options.parse_command_line()

    if options.t == 1:
        app = App()
        http_server = tornado.httpserver.HTTPServer(app)
        http_server.bind(options.port)
        http_server.start()
        tornado.ioloop.IOLoop.instance().start()
    elif options.t == 2:
        setting = {
            'debug' : options.debug
        }
        app = tornado.web.Application([
            ('/test',testHandler)    
            ],**setting)
        http_server = tornado.httpserver.HTTPServer(app)
        http_server.bind(options.port)
        http_server.start()
        tornado.ioloop.IOLoop.current().start()
    elif options.t == 3:
        setting = {
            'debug' : options.debug
        }
        app = tornado.web.Application([
            ('/test',testHandler)    
            ],**setting)
        app.listen(options.port)
        http_server.start()
        tornado.ioloop.IOLoop.current().start()




