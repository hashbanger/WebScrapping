
import scrapy
#from selenium import webdriver
#import time 
#from selenium.webdriver.common.keys import Keys
from ..items import QuoraquestItem

class QuoraSpider(scrapy.Spider):
    name = 'quora'
    allowed_domains = ['www.quora.com/topic/Job-Interviews']
    start_urls = ['http://www.quora.com/topic/Job-Interviews/']

    def parse(self, response):
        question = response.xpath('//*[@class="ui_qtext_rendered_qtext"]/text()').extract()

        for item in zip(question):
            new_item = QuoraquestItem()

            new_item['question'] = item[0]


            yield new_item
