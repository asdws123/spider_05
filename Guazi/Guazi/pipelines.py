# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class GuaziPipeline(object):
    def process_item(self, item, spider):
        #处理item数据
        print(item['name'],item['price'],item['link'])
        return item

class GuaziMongoPipeline(object):
    def open_spider(self,spider):
        '''爬虫开始时，链接mongo数据库'''
        self.conn = pymongo.MongoClient('localhost',27017)
        self.db = self.conn['guazidb']
        self.myset = self.db['guaziset']

    def process_item(self,item,spider):
        self.myset.insert_one(item)
        return item

