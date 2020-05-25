# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline(object):

    def __init__(self):
        self.file = open("1.txt", "wb")

    def process_item(self, item, spider):
        self.file.write(str(item).encode("utf-8"))
        self.file.flush()
        return item

    def __del__(self):
        self.file.close()
