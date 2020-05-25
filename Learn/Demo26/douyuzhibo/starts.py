# coding: utf-8

import scrapy
from scrapy import cmdline

cmdline.execute(["scrapy", "crawl", "douyujson", "-o", "douyu.json"])