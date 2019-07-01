# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

class GithubsSpider(scrapy.Spider):
    name = 'githubs'
    allowed_domains = ['www.github.com/hashbanger']
    start_urls = ['http://www.github.com/hashbanger/']
    def parse(self, response):
        yield Request(response, callback = self.parse)
    def parse(self, response):
        name = response.xpath('//*[@class = "repo js-pinnable-item"]/@title').extract_first()
        yield {'name': name}
