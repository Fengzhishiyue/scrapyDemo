# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import os
import json
import pymysql

from stock.spiders.stock import itemSpider


class StockPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonPipeline(object):
    def __init__(self):
        self.file = codecs.open(itemSpider.name+'.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "," + "\n"
        self.file.write(line)
        return item

    def open_spider(self, spider):
        self.file.write('[')

    def close_spider(self, spider):
        self.file.write(']')

    def spider_closed(self, spider):
        self.file.close()
