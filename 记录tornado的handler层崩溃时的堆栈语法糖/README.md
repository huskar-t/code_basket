# 记录tornado的handler层异常堆栈

#### 功能介绍
搭配异步log输出handler层的堆栈

#### 使用说明

class CreateAccountHandler(RequestHandler):
    @log_exception
    def post(self):

