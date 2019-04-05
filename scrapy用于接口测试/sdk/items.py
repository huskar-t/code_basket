# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SdkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class LoginItem(scrapy.Item):
    status = scrapy.Field()
    return_code = scrapy.Field()
    return_msg = scrapy.Field()