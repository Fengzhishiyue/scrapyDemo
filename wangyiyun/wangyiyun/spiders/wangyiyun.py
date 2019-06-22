#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import scrapy


class itemSpider(scrapy.Spider):
    name = "wangyiyun"
    allowed_domains = ["music.163.com"]
    start_urls = ["https://music.163.com/discover/playlist"]
    count = 1

    def parse(self, response):
        LL = response.css("#m-pl-container li")
        for l in LL:
            # 歌单名
            title = l.css(".u-cover .msk::attr(title)").extract_first()
            # 歌单地址
            listUrl = l.css(".u-cover .msk::attr(href)").extract()[0]
            listUrl = "https://music.163.com" + listUrl
            if self.count < 2:
                print("歌单地址：", listUrl)
                self.count += 1
                yield scrapy.Request(listUrl, callback=self.copyPage)

    # def copyPage(self, response):
    #     with open("歌单页面.html", "wb") as f:
    #         f.write(response.body)
    #     return
