# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com//']

    def parse(self, response):
        header_1 = response.xpath('//h1/a/text()').extract()
        tag_list = response.xpath('//*[@class = "tag-item"]/a/text()').extract()
        
        yield {'h1': header_1, 'tags': tag_list}
