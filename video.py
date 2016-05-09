from tornado.ioloop import IOLoop
from tornado.web import Application, RedirectHandler, RequestHandler, StaticFileHandler

from handlers import NavigationHandler

class MyHandler(RequestHandler):

    def get(self):
        self.write("""\
        <video controls preload="none" width="640" height="360">
          <source src="e04.mp4"  type="video/mp4">
        </video>
        """)


application = Application([
    (r"/", RedirectHandler, {"url": "/nav/"}),
    (r"/nav/(.*)", NavigationHandler),
    (r"/static/(.*)", StaticFileHandler, {"path": "/media/samba/0ADE833226CEC7BB/video_server"}),
])
loop = IOLoop.instance()
application.listen(8041)
loop.start()
