# coding: utf-8
import time

from tornado.ioloop import IOLoop, PeriodicCallback
from tornado.options import define, options
from tornado.web import Application
from handler import handlers
from session_manager import SessionMgr


class App(Application):
    def __init__(self):
        settings = dict(
            cookie_secret="awesome",
            # xsrf_cookie=True  # 同源策略
        )
        Application.__init__(self, handlers, **settings)


def main():
    define("host", "0.0.0.0", type=str)
    define("server_port", 9000, type=int)
    options.parse_command_line()

    app = App()
    app.listen(options.server_port)
    IOLoop.instance().start()
    # tornado循环任务每10秒进行主动心跳检测
    PeriodicCallback(SessionMgr().heartbeat, 10 * 1000).start()
if __name__ == '__main__':
    main()
