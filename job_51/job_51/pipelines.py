# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

class Job51Pipeline(object):
    MONGO_URL='mongodb://192.168.1.105:27017'

    def __init__(self):
        self.client=MongoClient(self.MONGO_URL)

    def process_item(self, item, spider):
        item['_id']=item['url']
        coll=self.client['zhao_pin']['51_job']
        if coll.find_one({"_id":item['_id']}):
            spider.logger.info('更新成功')
        else:
            coll.insert(item)
        return item
