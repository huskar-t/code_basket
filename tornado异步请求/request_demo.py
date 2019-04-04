# coding: utf-8
import traceback
from StringIO import StringIO
import json
from tornado.gen import coroutine
from tornado.httpclient import AsyncHTTPClient


class Request(object):
    @coroutine
    def post(self, url, body):
        try:
            request = AsyncHTTPClient()
            response = yield request.fetch(url, method="POST", body=body)
            print("url: {0} body {1}".format(url, response))
        except Exception:
            fp = StringIO()
            traceback.print_exc(file=fp)
            print("url: {0} fail: {1}".format(url, fp.getvalue()))

    @coroutine
    def demo_post(self, data):
        print(111)
        url = "127.0.0.1:8080/demo"
        body = json.dumps(data)
        self.post(url, body)
