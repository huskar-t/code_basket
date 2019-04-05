# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SdkPipeline(object):
    def process_item(self, item, spider):
        return item


class LoginPipeline(object):
    def process_item(self, item, spider):
        with open("login.txt", 'a') as fp:
            fp.write(str(item['status']) + '\t'
                     + item['return_code'] + '\t'
                     + item['return_msg'] + '\t' + '\n')
