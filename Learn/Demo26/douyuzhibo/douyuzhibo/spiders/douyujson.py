# -*- coding: utf-8 -*-
import json

import scrapy
from douyuzhibo.items import DouyuzhiboItem


class DouyujsonSpider(scrapy.Spider):
    name = 'douyujson'
    allowed_domains = ['capi.douyucdn.cn']
    start_urls = ['http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset=0']
    offset = 0

    def parse(self, response):
        data = json.loads(response.text)["data"]
        for dataline in data:
            dataitem = DouyuzhiboItem()
            dataitem["name"] = dataline["nickname"]
            dataitem["image_src"] = dataline["vertical_src"]
            yield dataitem
        if self.offset < 240:
            self.offset += 20
            yield scrapy.Request("http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset={}".format(self.offset), callback=self.parse)
