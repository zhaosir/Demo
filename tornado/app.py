#! /usr/bin/env python
# -*- coding : utf-8 -*-

import tornado
import tornado.web
import time
import tornado.httpserver
import tornado.ioloop
from tornado.options import define,options


class testHandler(tornado.web.RequestHandler):
    def get(self):
        self.write({
                    'code' : 1,
                    'time' : int(time.time())
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




