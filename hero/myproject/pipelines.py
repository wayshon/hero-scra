# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
import json

class MyprojectPipeline(object):
    
    def process_item(self, item, spider):
        if (item.get('title') is not None and item.get('href') is not None):
            return item
        else:
            pass

class MongoDBPipeline(object):
    """
    将item写入MongoDB
    """

    @classmethod
    def from_crawler(cls, crawler):
        cls.MONGODB_SETTINGS = crawler.settings.get('MONGODB_SETTINGS')
        return cls()

    def open_spider(self, spider):
        dbname = self.MONGODB_SETTINGS['db']
        host = self.MONGODB_SETTINGS['host']
        port = self.MONGODB_SETTINGS['port']
        username = self.MONGODB_SETTINGS['username']
        password = self.MONGODB_SETTINGS['password']
        self.client = MongoClient(host=host,port=port,username=username,password=password,authSource=dbname,authMechanism='SCRAM-SHA-1')
        self.db = self.client[dbname]
        self.collection = self.db['zufang']

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item