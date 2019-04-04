# coding: utf-8

import json
import os
import socket
import sys
try:
    syslog = __import__("syslog")
except ImportError:
    syslog = None

import zmq
from tornado.options import options


__all__ = ["Logger"]


# noinspection PyBroadException
def frame():
    try:
        raise Exception
    except:
        return sys.exc_info()[2].tb_frame.f_back


if hasattr(sys, '_getframe'):
    # noinspection PyProtectedMember
    frame = lambda: sys._getframe(3)

CRITICAL = 60
FATAL = 50
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

level_names = {
    CRITICAL: 'CRITICAL',
    ERROR: 'ERROR',
    WARNING: 'WARNING',
    INFO: 'INFO',
    DEBUG: 'DEBUG',
    NOTSET: 'NOTSET',
    FATAL: 'FATAL',
    'CRITICAL': CRITICAL,
    'ERROR': ERROR,
    'WARN': WARNING,
    'WARNING': WARNING,
    'INFO': INFO,
    'DEBUG': DEBUG,
    'NOTSET': NOTSET,
    'FATAL': FATAL,
}
_srcfile = os.path.normcase(frame.__code__.co_filename).capitalize()
host = socket.gethostbyname(socket.gethostname())
context = zmq.Context()
tcp_url = "tcp://127.0.0.1:{0}".format(options.logger_port)

zmq_socket = context.socket(zmq.PUSH)
zmq_socket.connect(tcp_url)


class Logger(object):
    """
    生产者
    """

    def __init__(self, ):
        self.pid = os.getpid()
        self.host = host
        self.level = None
        self.line = None
        self.msg = None
        self.remote_ip = ""

    def file_descriptor(self):
        """
        Find the stack frame of the caller so that we can note the source
        file name, line number and function name.
        """
        f = frame()
        # On some versions of IronPython, currentframe() returns None if
        # IronPython isn't run with -X:Frames.
        if f is not None:
            f = f.f_back

        rv = "(unknown file)", 0, "(unknown function)"
        while hasattr(f, "f_code"):
            co = f.f_code
            filename = os.path.normcase(co.co_filename).capitalize()
            if filename == _srcfile:
                f = f.f_back
                continue
            rv = (co.co_filename, f.f_lineno, co.co_name)
            break
        self.line = "{0}:{2}[{1}]".format(*rv)

    def debug(self, msg):
        self.level = DEBUG
        self.msg = msg
        self.record()

    def info(self, msg):
        self.level = INFO
        self.msg = msg
        self.record()

    def warn(self, msg):
        self.level = WARN
        self.msg = msg
        self.record()

    def fatal(self, msg):
        self.level = FATAL
        self.msg = msg
        self.record()

    def critical(self, msg):
        self.level = CRITICAL
        self.msg = msg
        self.record()

    def record(self):
        self.file_descriptor()
        record_format = json.dumps({
            "level": level_names[self.level],
            "remote_ip": self.remote_ip,
            "line": self.line,
            "msg": self.msg,
        })
        self.producer(record_format)
        self.reset()

    def set_remote_ip(self,remote_ip):
        self.remote_ip = remote_ip

    def reset(self):
        self.level = None
        self.line = None
        self.msg = None
        self.remote_ip = ""

    def producer(self, record):
        zmq_socket.send(record)
