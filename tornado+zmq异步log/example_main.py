# coding: utf-8
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application, RequestHandler


class CreateAccountHandler(RequestHandler):
    def post(self):
        # log使用
        self.application.logger.critical("log使用")


handlers = [
    (r"/web/create_account", CreateAccountHandler),  # 创建账号
]


class App(Application):
    def __init__(self):
        settings = dict(
            cookie_secret="awesome",
            # xsrf_cookie=True  # 同源策略
        )
        Application.__init__(self, handlers, **settings)

        # 绑定生产者
        from utils.logger import Logger
        self.logger = Logger()


def main():
    define("host", "0.0.0.0", type=str)
    define("server_port", 9000, type=int)
    define("logger_port", 8047, type=int)
    options.parse_command_line()

    app = App()
    app.listen(options.server_port)
    IOLoop.instance().start()


if __name__ == '__main__':
    main()
