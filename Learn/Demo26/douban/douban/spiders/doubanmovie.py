# -*- coding: utf-8 -*-
import scrapy
from douban import items


class DoubanmovieSpider(scrapy.Spider):
    name = 'doubanmovie'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0']
    offset = 0

    def parse(self, response):

        movies = response.xpath("//div[@class='info']")
        for movie in movies:
            doubanitem = items.DoubanItem()
            doubanitem["title"] = movie.xpath(".//span[@class='title'][1]/text()").extract()
            doubanitem["info"] = movie.xpath(".//div[@class='bd']//p/text()").extract()
            doubanitem["star"] = movie.xpath(".//div[@class='star']/span[@class='rating_num']/text()").extract()
            quote = movie.xpath(".//p[@class='quote']/span[@class='inq']/text()").extract()
            if len(quote) != 0:
                doubanitem['quote'] = quote[0]
            else:
                doubanitem['quote'] = None
            yield doubanitem
        if self.offset < 225:
            self.offset += 25
        yield scrapy.Request('https://movie.douban.com/top250?start={}'.format(self.offset))

