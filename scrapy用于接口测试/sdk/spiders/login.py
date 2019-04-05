# coding:utf-8
import base64
import hashlib
import json
from scrapy import Request
from scrapy.spiders import Spider


# scrapy crawl login --nolog
from sdk.items import LoginItem


class LoginSpider(Spider):
    name = "login"
    start_urls = [
        r"http://127.0.0.1:8080/v1/user/register"
    ]*100

    def start_requests(self):
        data = {
            "account": "123456",
            "game_appid": "ASDASD",
            "game_id": "31",
            "game_name": "演示",
            "password": "123456",
            "promote_account": "自然注册",
            "promote_id": "0",
            "sdk_version": "1",
        }
        sign = get_sign(data)
        data["md5_sign"] = sign
        data_sign = base64.b64encode(json.dumps(data).encode("utf-8"))
        for url in self.start_urls:
            yield Request(url, method="POST", body=data_sign,
                          callback=self.parse_page, dont_filter=True)

    def parse_page(self, response):
        body = json.loads(response.body)
        print(body)
        item = LoginItem()
        item["status"] = body["status"]
        item["return_code"] = body["return_code"]
        item["return_msg"] = body["return_msg"]
        yield item
def get_sign(dic):
    sort_keys = sorted(dic.keys())
    v = ""
    for k in sort_keys:
        v += str(dic[k])
    if v != "":
        v += "mengchuang"
    m = hashlib.md5()
    m.update(v.encode())
    return m.hexdigest()
