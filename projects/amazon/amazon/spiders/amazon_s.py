# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonItem

class AmazonSSpider(scrapy.Spider):
    name = 'amazon_s'
    allowed_domains = ['https://www.amazon.in/s?k=machine+learing&ref=nb_sb_noss_2']
    start_urls = ['http://www.amazon.in/s?k=machine+learing&ref=nb_sb_noss_2/']

    def parse(self, response):
        all_titles = response.xpath('//h2/a/span/text()').extract()
        price = response.css('.a-price-whole::text').extract()
        rating = response.css('.a-icon-alt::text').extract()

        for item in zip(all_titles, price, rating):
            new_item = AmazonItem()

            new_item['title'] = item[0]
            new_item['price'] = item[1]
            new_item['rating'] = item[2]

            yield new_item
