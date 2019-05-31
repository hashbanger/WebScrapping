# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class BooksSpider(CrawlSpider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com']

    rules = (Rule(LinkExtractor(deny_domains = ('google.com')), callback = 'parse_page', follow = False),)
    # To include links with chosen keyword use the LinkExtracotr argument "allow = 'keyword'" ,
    
    def parse_page(self, response):
        pass
