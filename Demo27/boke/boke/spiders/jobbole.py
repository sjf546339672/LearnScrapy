# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['jobbole.com']  # 不在列表中的url剔除掉
    start_urls = ['http://jobbole.com/']

    def parse(self, response):

        pass
