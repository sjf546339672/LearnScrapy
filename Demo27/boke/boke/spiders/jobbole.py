# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['jobbole.com']  # 不在列表中的url剔除掉
    start_urls = ['http://jobbole.com/caijing/']

    def parse(self, response):
        print(response)
        print(type(response))
        with open("jobbole.html", "wb") as fp:
            fp.write(response.body)