import tornado.ioloop
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        path = self.get_argument('path', './')
        #abs_path = os.path.abspath(path)
        dir_list = os.listdir(path)
        self.render('dir_list.html', dir_list = dir_list)

if __name__ == '__main__':
    app = tornado.web.Application([
        (r"/", MainHandler),
        (r'/(.*)', tornado.web.StaticFileHandler, {'path': './'})
    ])

    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()