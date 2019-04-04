#coding:utf-8
from tornado.gen import coroutine
from tornado.ioloop import PeriodicCallback, IOLoop


# 定时任务
def do_something():
    pass


PeriodicCallback(do_something, 1000).start()
# 延时任务
def do_something_after(ss):
    print(ss)

timer = IOLoop().instance().add_timeout(3, do_something_after, 3)

# 协程
@coroutine
def demo_coroutine():
    yield 123
