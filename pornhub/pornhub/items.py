# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PornhubItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 名字
    name = scrapy.Field()
    # 图片地址
    imageUrl = scrapy.Field()
    # 链接地址
    linkUrl = scrapy.Field()
    # 播放量
    playNum = scrapy.Field()
    # 推荐度
    recommendation = scrapy.Field()
    # 时长
    time = scrapy.Field()
