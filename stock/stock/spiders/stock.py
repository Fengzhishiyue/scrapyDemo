#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import scrapy

from stock.items import StockItem


class itemSpider(scrapy.Spider):
    name = 'stock'
    
    start_urls = ['http://quote.stockstar.com/stock/ranklist_a_3_1_1.html']

    def parse(self, response):
        page = response.body
        testCss = response.css('#datalist tr')
        for t in testCss:
            # 创建对象
            item = StockItem()
            # 股票代码
            stockId = t.css('td a::text').extract()[0]
            # 简称
            Abbreviation = t.css('td a::text').extract()[1]
            # 最新价
            latestPrice = t.css('td span::text').extract()[0]
            latestPrice = float(latestPrice)
            # 涨跌幅
            quoteChange = t.css('td span::text').extract()[1]
            quoteChange = round(float(quoteChange.strip('%'))/100, 4)
            # 涨跌额
            amountChange = t.css('td span::text').extract()[2]
            amountChange = float(amountChange)
            # 5分钟涨幅
            increase = t.css('td span::text').extract()[3]
            increase = round(float(increase.strip('%'))/100, 4)
            # 成交量
            volume = t.css('td::text').extract()[0]
            volume = float(volume)
            # 成交额
            turnover = t.css('td::text').extract()[1]
            turnover = float(turnover)
            # 换手率
            handTurnoverRate = t.css('td::text').extract()[2]
            handTurnoverRate = round(float(handTurnoverRate.strip('%'))/100, 4)
            # 振幅
            amplitude = t.css('td::text').extract()[3]
            amplitude = round(float(amplitude.strip('%'))/100, 4)
            # 量比
            volumeRatio = t.css('td::text').extract()[4]
            volumeRatio = float(volumeRatio)
            # 委比
            commission = t.css('td::text').extract()[5]
            commission = float(commission)
            # 市盈率
            PERatio = t.css('td::text').extract()[6]
            if (PERatio == '--'):
                PERatio = float("0")
            else:
                PERatio = float(PERatio)

            item['stockId'] = stockId
            item['Abbreviation'] = Abbreviation
            item['latestPrice'] = latestPrice
            item['quoteChange'] = quoteChange
            item['amountChange'] = amountChange
            item['increase'] = increase
            item['volume'] = volume
            item['turnover'] = turnover
            item['handTurnoverRate'] = handTurnoverRate
            item['amplitude'] = amplitude
            item['volumeRatio'] = volumeRatio
            item['commission'] = commission
            item['PERatio'] = PERatio

            # text = stockId+"   "+Abbreviation
            # print(text)
            yield item

        # with open('股票.html', 'wb') as f:  # python文件操作，不多说了；
        #     f.write(page)  # 刚才下载的页面去哪里了？response.body就代表了刚才下载的页面！
