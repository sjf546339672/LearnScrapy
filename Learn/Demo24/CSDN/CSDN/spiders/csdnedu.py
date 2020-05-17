# -*- coding: utf-8 -*-
# import scrapy
# import CSDN.items
#
#
# class CsdneduSpider(scrapy.Spider):
#     name = 'csdnedu'
#     allowed_domains = ['www.csdn.net']
#     start_urls = ['https://edu.csdn.net/lecturer?&page=1']
#     offset = 1
#
#     def parse(self, response):
#         csdnitems = CSDN.items.CsdnItem()
#         csdnitems["name"] = response.xpath("//ul[@class='list-inline clearfix']//li[1]/a/text()").extract()
#         csdnitems["lesson"] = response.xpath("//ul[@class='list-inline clearfix']//li[2]/span/text()").extract()
#         csdnitems["students_numbers"] = response.xpath("//ul[@class='list-inline clearfix']//li[3]/span/text()").extract()
#         csdnitems["description"] = response.xpath("//dd[@class='cont']/p/text()").extract()
#         if self.offset <= 30:
#             self.offset += 1
#         newurl = "https://edu.csdn.net/lecturer?&page={}".format(self.offset)
#         yield scrapy.Request(newurl, self.parse)  # 翻页自己调用自己
import urllib2

import scrapy
import CSDN.items

# import urllib.request
import urllib
import lxml
import lxml.etree
import re


class CsdneduSpider(scrapy.Spider):
    name = 'csdnedu'
    allowed_domains = ['edu.csdn.net']
    start_urls = ['http://edu.csdn.net/lecturer?&page=1']
    offset=1

    def parse(self, response):
        mytree=response
        nodedata= mytree.xpath("//*[@class=\"panel-body\"]//dl/dd/p/text()").extract()
        nodename = mytree.xpath("//*[@class=\"panel-body\"]//dl/dd/ul//li[1]/a/text()").extract()
        nodelessions = mytree.xpath("//*[@class=\"panel-body\"]//dl/dd/ul//li[2]/span/text()").extract()
        nodestudents= mytree.xpath("//*[@class=\"panel-body\"]//dl/dd/ul//li[3]/span/text()").extract()
        for i   in range(len(nodedata)):
            csdnitem=CSDN.items.CsdnItem()
            csdnitem["name"]=nodename [i]
            csdnitem["lessons"]=nodelessions[i]
            csdnitem["students"]=nodestudents [i]
            csdnitem["title"]=nodedata[i]
            yield  csdnitem

        if self.offset <=32:
            self.offset+=1

        newurl="http://edu.csdn.net/lecturer?&page="+str(self.offset)
        yield scrapy.Request(newurl,self.parse) #翻页，自己调用自己，