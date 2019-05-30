# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.loader import ItemLoader
import scrapy
from Quotes.items import QuotesItem

class QuotesSpider(Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        l = ItemLoader(item = QuotesItem(), response = response)
        quotes = response.xpath('//*[@class = "quote"]')
        
        # iterating over each individual quote class
        for quote in quotes:
            text = quote.xpath('.//*[@class = "text"]/text()').extract_first()
            author = quote.xpath('.//*[@class = "author"]/text()').extract_first()
            tags = quote.xpath('.//*[@itemprop = "keywords"]/@content').extract_first()

            # yield{'Text': text,
            #       'Author': author,
            #       'Tags': tags}

            l.add_value('Text',text)      # Keys must be same as defined in items.py
            l.add_value('Author',author)
            l.add_value('Tags',tags)

        
        
        # Now we append the path of the next page
        next_page_url = response.xpath('//*[@class = "next"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url) # outside the parse function the callback will also be needed
        
        print(l.load_item())
