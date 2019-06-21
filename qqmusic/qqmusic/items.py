# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QqmusicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    playNum = scrapy.Field()
    author = scrapy.Field()
    imgUrl = scrapy.Field()
    # https://music.163.com/playlist?id=2836499019
    listUrl = scrapy.Field()

