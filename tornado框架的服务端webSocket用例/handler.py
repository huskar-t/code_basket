# coding:utf-8
import time
from tornado.websocket import WebSocketHandler
from session_manager import SessionMgr

# noinspection PyAbstractClass
class WSServer(WebSocketHandler):
    last_time = 0

    def check_origin(self, origin):
        # 跨域
        return True

    def open(self, *args, **kwargs):
        # 创建连接时进行操作
        SessionMgr().add(self)
        pass

    def on_close(self):
        # 客户端断开或服务端断开后操作
        pass
    def on_message(self, buf):
        # 有消息到来时
        self.last_time = time.time()
        pass


handlers = [
    (r"/webSocket", WSServer),
]
