# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CsdnItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # lesson = scrapy.Field()
    # students_numbers = scrapy.Field()
    # description = scrapy.Field()
    name = scrapy.Field()
    lessons = scrapy.Field()
    students = scrapy.Field()
    title = scrapy.Field()

