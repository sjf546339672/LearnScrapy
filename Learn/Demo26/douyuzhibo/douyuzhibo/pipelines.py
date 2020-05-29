# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import urllib
from urllib import request


class DouyuzhiboPipeline:
    def process_item(self, item, spider):
        print(item["image_src"])
        templist = item["image_src"].split("/")
        if "dy1" in item["image_src"]:
            urllib.request.urlretrieve(item["image_src"], "E:\AllProject\MyProject\LearnScrapy\Learn\Demo26\douyuzhibo\douyuzhibo\pic\\" + templist[len(templist) - 2])
        else:
            urllib.request.urlretrieve(item["image_src"], "E:\AllProject\MyProject\LearnScrapy\Learn\Demo26\douyuzhibo\douyuzhibo\pic\\" + templist[len(templist) - 1])
        return item
