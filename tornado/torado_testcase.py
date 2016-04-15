import tornado.web, tornado.gen, tornado.httpclient, tornado.testing
import unittest

class GenHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        response = yield tornado.gen.Task(http.fetch, 'http://www.baidu.com')
        self.write('1')
        self.finish()

# code for run nose test
class GenTestCase(unittest.TestCase):
    def setUp(self):
        application = tornado.web.Application([(r'/test', GenHandler)])
        self.http_server = tornado.httpserver.HTTPServer(application)
        self.http_server.listen(8888)

    def tearDown(self):
        self.http_server.stop()

#    def get_app(self):
#        return tornado.web.Application([(r'/gen', GenHandler)])
#    def test_gen(self):
#        response = self.fetch(r'/gen')
#        print 'xxxx'
#        assert response.code == 200

    def handle_request(self, response):
        self.response = response
        tornado.ioloop.IOLoop.instance().stop()

    def testHelloWorldHandler(self):
        http_client = tornado.httpclient.AsyncHTTPClient()
        http_client.fetch('http://localhost:8888/test', self.handle_request)
        tornado.ioloop.IOLoop.instance().start()
        print self.response.body

#    def get_new_ioloop(self):
#        return tornado.ioloop.IOLoop.instance()

# code for run standalone
#application = tornado.web.Application([(r'/gen', GenHandler),])
if __name__ == "__main__":
    unittest.main()
#    application.listen(8888)
#    tornado.ioloop.IOLoop.instance().start()
