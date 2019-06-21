#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import scrapy
import codecs
import os
import json
import pymysql

from qqmusic.items import QqmusicItem


class itemSpider(scrapy.Spider):
    name = "qqmusic"
    allowed_domains = ["music.163.com"]
    custom_settings = {
        "ITEM_PIPELINES": {
            "qqmusic.pipelines.JsonPipeline": 200,
            "qqmusic.pipelines.mysqlPipeline": 100,
            "qqmusic.pipelines.imagePipeline": 300
        },
        "FILES_STORE": "/Users/mac/Desktop/p/pyCode/imgs",  # 文件存储路径
        "IMAGES_STORE": "/Users/mac/Desktop/p/pyCode/imgs",  # 图片存储路径
        # 避免下载最近90天已经下载过的文件内容
        "FILES_EXPIRES": 90,
        # 避免下载最近90天已经下载过的图像内容
        "IMAGES_EXPIRES": 30,
        # 设置图片缩略图
        "IMAGES_THUMBS": {"small": (50, 50), "big": (250, 250)},
        # 图片过滤器，最小高度和宽度，低于此尺寸不下载
        "IMAGES_MIN_HEIGHT": 110,
        "IMAGES_MIN_WIDTH": 110,
    }

    start_urls = ["https://music.163.com/discover/playlist"]

    def parse(self, response):
        LL = response.css("#m-pl-container li")
        for l in LL:
            item = QqmusicItem()
            # 图片地址
            imgUrl = l.css(".u-cover img::attr(src)").extract_first()
            # 歌单名
            title = l.css(".u-cover .msk::attr(title)").extract_first()
            # 歌单地址
            listUrl = l.css(".u-cover .msk::attr(href)").extract()[0]
            listUrl = "https://music.163.com" + listUrl
            # 播放数量
            playNum = l.css(".u-cover .nb::text").extract()[0]
            if "万" in playNum:
                playNum = int(playNum.split("万")[0]) * 10000
            else:
                playNum = int(playNum)
            # 作者
            author = l.css(".nm::text").extract()[0]
            item["imgUrl"] = imgUrl
            item["title"] = title
            item["listUrl"] = listUrl
            item["playNum"] = playNum
            item["author"] = author
            yield item

