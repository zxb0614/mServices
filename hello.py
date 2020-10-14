from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler


class Indexhandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("<h3>Hello</h3>")

if __name__ == '__main__':
    app = Application([
        ('/',Indexhandler)
    ]
    )
    app.listen(7000)
    print("starting http://localhost:%s"%7000)
    IOLoop.current().start()