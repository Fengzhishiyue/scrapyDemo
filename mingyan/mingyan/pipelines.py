# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import os
import json
import pymysql
from mingyan.items import MingyanItem
from mingyan.spiders.test2 import itemSpider


class MingyanPipeline(object):
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


class mysqlPipeline(object):
    def process_item(self, item, spider):
        '''
        将爬取的信息保存到mysql
        '''
        # 将item里的数据拿出来
        textss = item['text']
        autor = item['autor']
        tags = item['tags']

        # 和本地的newsDB数据库建立连接
        db = pymysql.connect(
            host='localhost',  # 连接的是本地数据库
            user='root',  # 自己的mysql用户名
            passwd='root',  # 自己的密码
            db='pc',  # 数据库的名字
            charset='utf8',  # 默认的编码方式：
            cursorclass=pymysql.cursors.DictCursor)
        try:
            # 使用cursor()方法获取操作游标
            cursor = db.cursor()
            # SQL 插入语句
            sql = "INSERT INTO TEST2(text,autor,tags) \
                  VALUES ('%s', '%s', '%s')" % (textss, autor, tags)
            # 执行SQL语句
            cursor.execute(sql)
            # 提交修改
            db.commit()
        finally:
            # 关闭连接
            db.close()
        return item
