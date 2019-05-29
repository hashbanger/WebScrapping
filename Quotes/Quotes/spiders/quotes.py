# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath('//*[@class = "quote"]')
        # iterating over each individual quote class
        for quote in quotes:
            text = quote.xpath('.//*[@class = "text"]/text()').extract_first()
            author = quote.xpath('.//*[@class = "author"]/text()').extract_first()
            tags = quote.xpath('.//*[@itemprop = "keywords"]/@content').extract_first()

            yield{'Text': text,
                  'Author': author,
                  'Tags': tags}
              
            # Now we append the path of the next page

        next_page_url = response.xpath('//*[@class = "next"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url) # outside the parse function the callback will also be needed