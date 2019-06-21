# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StockItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    stockId = scrapy.Field()  # 代码
    Abbreviation = scrapy.Field()  # 简称
    latestPrice = scrapy.Field()  # 最新价
    quoteChange = scrapy.Field()  # 涨跌幅
    amountChange = scrapy.Field()  # 涨跌额
    increase = scrapy.Field()  # 5分钟涨幅
    volume = scrapy.Field()  # 成交量
    turnover = scrapy.Field()  # 成交额
    handTurnoverRate = scrapy.Field()  # 换手率
    amplitude = scrapy.Field()  # 振幅
    volumeRatio = scrapy.Field()  # 量比
    commission = scrapy.Field()  # 委比
    PERatio = scrapy.Field()  # 市盈率
