# coding:utf-8
import functools
import traceback
from StringIO import StringIO

def log_exception(fn):
    """记录handler层异常log"""
    @functools.wraps(fn)
    def wrapper(self, *args, **kwargs):
        try:
            fn(self, *args, **kwargs)
        except Exception:
            fp = StringIO()
            traceback.print_exc(file=fp)
            # 下面这行是使用异步log的例子可以换其他log输出
            self.application.logger.critical(fp.getvalue())
    return wrapper
