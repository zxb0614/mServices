import tornado.web
from tornado.ioloop import IOLoop
import tornado.options



class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):

        self.write('<h3>hello,我是主页</h3>')


def make_app():
    return  tornado.web.Application([('/',IndexHandler),
                                     ],
                                    default_host=tornado.options.options.host)


if __name__ == '__main__':
    tornado.options.define('port',default=8000,type=int,help='bind socket port')
    tornado.options.define('host', default='localhost', type=str, help='设置host name')
    tornado.options.parse_command_line()
    app = make_app()
    app.listen(tornado.options.options.port)
    print('starting http:%s:%s'%(tornado.options.options.host,tornado.options.options.port))
    IOLoop.current().start()