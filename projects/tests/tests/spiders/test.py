# -*- coding: utf-8 -*-
import scrapy
from ..items import TestsItem


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['books.toscrape.com/']
    start_urls = ['http://books.toscrape.com//']

    def parse(self, response):
        nextpageurl = response.xpath('//*[@class = "next"]/a/@href')

        for item in self.scrape(response):
            yield item

        if nextpageurl:
            path = nextpageurl.extract_first()
            # nextpage = "http://www.99acres.com" + path
            nextpage = response.urljoin(path)
            print("Found url: {}".format(nextpage))
            yield scrapy.Request(nextpage, callback=self.parse)

    def scrape(self, response):
        price = response.xpath('//*[@class = "srpNw_price "]/text()').extract()

        for items in zip(price):
            new_item = NinenineacresItem()
            new_item['price'] = items[0]

            yield new_item
