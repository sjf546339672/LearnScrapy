# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()  # 标题
    info = scrapy.Field()  # 信息
    star = scrapy.Field()  # 评分星级
    quote = scrapy.Field()  # 评价

