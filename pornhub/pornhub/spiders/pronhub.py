#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import scrapy

from pornhub.items import PornhubItem


class itemSpider(scrapy.Spider):
    name = "pornhub"
    start_urls = ["https://www.pornhub.com/video?o=ht"]

    custom_settings = {"ITEM_PIPELINES": {"pornhub.pipelines.JsonPipeline": 200}}
    count = 1

    def parse(self, response):
        LL = response.css("#videoCategory .wrap")
        for l in LL:
            item = PornhubItem()
            item["imageUrl"] = l.css("img::attr(data-thumb_url)").extract()[0]
            item["linkUrl"] = (
                "https://www.pornhub.com" + l.css(".title a::attr(href)").extract()[0]
            )
            item["name"] = l.css(".title a::text").extract()[0]
            item["playNum"] = l.css(".videoDetailsBlock var::text").extract()[0]
            item["recommendation"] = l.css(".videoDetailsBlock .value::text").extract()[
                0
            ]
            item["time"] = l.css(".duration::text").extract()[0]
            yield item
            # https://www.pornhub.com
        nextP1 = response.css(".page_next a::attr(href)").extract()[0]
        nextP = "https://www.pornhub.com" + nextP1
        if self.count < 20:  # 判断是否存在下一页
            self.count += 1
            yield scrapy.Request(nextP, callback=self.parse)
