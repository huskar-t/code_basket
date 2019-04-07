# coding:utf-8

"""
tornado模板使用初探(为什么不做前后端分离啊!这么牺牲异步性能真的好吗?)
"""

from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application, RequestHandler


class TempHandler(RequestHandler):
    def get(self):
        render_data = {
            "title": "MAX",
            "items": ("item1",
                      "item2",
                      "item3")

        }
        self.render("temp.html", **render_data)


handlers = [
    (r"/", TempHandler),
]


class App(Application):
    def __init__(self):
        settings = dict(
            template_path='templates',  # 模板
            static_path='static',  # 静态文件
        )
        Application.__init__(self, handlers, **settings)


def main():
    define("host", "0.0.0.0", type=str)
    define("server_port", 9000, type=int)
    options.parse_command_line()

    app = App()
    app.listen(options.server_port)
    IOLoop.instance().start()


if __name__ == '__main__':
    main()
