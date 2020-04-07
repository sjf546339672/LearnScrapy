# coding: utf-8

import scrapy


class BooksSpider(scrapy.Spider):
    name = "houses"
    start_urls = ['https://newhouse.fang.com/house/s/']

    def parse(self, response):

        for i in range(1, 10):
            next_url = 'https://newhouse.fang.com/house/s/b9' + str(i) + '/'
            for house in response.css('div.nlc_details'):
                name = house.xpath(
                    './/div[@class="address"]/a/@title').extract_first()
                price = house.xpath(
                    './/div[@class="nhouse_price"]/span/text()').extract_first()
                unit = house.xpath(
                    './/div[@class="nhouse_price"]/em/text()').extract_first()
                yield {
                    'name': name,
                    'price': price,
                    '单位': unit
                }

            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url, callback=self.parse)
