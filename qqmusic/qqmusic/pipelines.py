# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import os

import pymysql
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline  # 内置的图片管道


class QqmusicPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonPipeline(object):
    def __init__(self):
        self.file = codecs.open("songList.json", "w", encoding="utf-8")

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "," + "\n"
        self.file.write(line)
        return item

    def open_spider(self, spider):
        self.file.write("[")

    def close_spider(self, spider):
        self.file.write("]")

    def spider_closed(self, spider):
        self.file.close()


class mysqlPipeline(object):
    def process_item(self, item, spider):
        """
        将爬取的信息保存到mysql
        """
        # 将item里的数据拿出来
        imgUrl = item["imgUrl"]
        title = item["title"]
        listUrl = item["listUrl"]
        playNum = item["playNum"]
        author = item["author"]
        # 和本地的newsDB数据库建立连接
        db = pymysql.connect(
            host="localhost",  # 连接的是本地数据库
            user="root",  # 自己的mysql用户名
            passwd="root",  # 自己的密码
            db="pc",  # 数据库的名字
            charset="utf8",  # 默认的编码方式：
            cursorclass=pymysql.cursors.DictCursor,
        )
        try:
            # 使用cursor()方法获取操作游标
            cursor = db.cursor()
            # SQL 插入语句
            sql = (
                "INSERT INTO songList(imgUrl,title,listUrl,author,playNum) \
                  VALUES ('%s', '%s', '%s','%s','%d')"
                % (imgUrl, title, listUrl, author, playNum)
            )
            # 执行SQL语句
            cursor.execute(sql)
            # 提交修改
            db.commit()
        finally:
            # 关闭连接
            db.close()
        return item


# 存储图片
class imagePipeline(ImagesPipeline):  # 继承ImagesPipeline这个类
    # 获取下载地址和文件名
    def get_media_requests(self, item, info):
        imgUrl = item["imgUrl"]
        yield scrapy.Request(imgUrl, meta={"name": item["title"]})

    def item_completed(self, results, item, info):
        image_paths = [x["path"] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item

    # 设置文件名
    def file_path(self, request, response=None, info=None):
        name = request.meta["name"] + ".jpg"
        down_file_name = u"full/{0}/{1}".format("网易云歌单", name)
        return down_file_name
