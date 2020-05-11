# -*- coding: utf-8 -*-
import scrapy
import Tencent.items


class HrtencentSpider(scrapy.Spider):
    name = 'hrTencent'
    allowed_domains = ['careers.tencent.com']
    start_urls = ['https://careers.tencent.com/search.html?keyword=python']

    def parse(self, response):
        for everydata in response.xpath('//div[@class="recruit-list"]'):
            print("================")
            print(everydata)
            print("================")
            tencentitem = Tencent.items.TencentItem()
            tencentitem["name"] = everydata.xpath("./a/h4/text()")
            tencentitem["date"] = everydata.xpath("./a/p[@class='recruit-tips']/span[3]/text()")
            tencentitem["content"] = everydata.xpath("./a/p[@class='recruit-text'/text()]")
            print("=========================")
            print(tencentitem["name"])
            print(tencentitem["date"])
            print(tencentitem["content"])
            print("=========================")
            # yield tencentitem


