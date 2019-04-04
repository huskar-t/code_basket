# coding: utf-8
import time

class Singleton(type):
    def __init__(cls, name, bases, class_dict):
        super(Singleton, cls).__init__(name, bases, class_dict)
        cls._instance = None

    def __call__(cls, *args):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args)
        return cls._instance


class SessionMgr(object):
    # 单例模式
    __metaclass__ = Singleton

    def __init__(self):
        self.session_set = set()

    def add(self, session):
        self.session_set.add(session)

    def delete(self, session):
        self.session_set.remove(session)

    def heartbeat(self):
        # 服务端主动检查心跳,30s超时
        heartbeat = 30
        now = time.time()
        expire_session_set = set()
        for session in self.session_set:
            try:
                if now - session.last_time > heartbeat:
                    session.close()
                    expire_session_set.add(session)
            except Exception:
                pass
        map(self.delete, expire_session_set)
