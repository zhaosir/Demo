#! /usr/bin/env python
# -*- coding:utf-8 -*-


import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop

cl = {}

class WebSocketHandler(tornado.websocket.WebSocketHandler):
	def check_origin(self,origin):
		return True

	def open(self):
		cid = self.get_argument('id')
		print 'open:' , cid
#		if self not in cl:
#			cl.append(self)

		if cid and not cl.has_key(cid):
			cl[cid] = self

	def on_message(self,message):
		self.write_message('message:' + message)

	def on_close(self):
		cid = self.get_argument('id')
		print 'close:' , cid
#		if self in cl:
#			cl.remove(self)
		if cid and cl.has_key(cid):
			del cl[cid]


class ApiHandler(tornado.web.RequestHandler):
	def get(self):
		msg = self.get_argument('msg',None)
		cid = self.get_argument('cid',None)
		if cl.has_key(cid):
			cl[cid].write_message(msg)
#		for c in cl.iteritems():
#			c.write_message(msg)

class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r'/ws',WebSocketHandler),
			(r'/api',ApiHandler)
		]

		tornado.web.Application.__init__(self,handlers)


if __name__ == "__main__":
	app = Application()
	server = tornado.httpserver.HTTPServer(app)
	server.listen(8100)
	tornado.ioloop.IOLoop.instance().start()
