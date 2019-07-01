
import scrapy
from selenium import webdriver
import time
#from selenium.webdriver.common.keys import Keys
from ..items import QuoraquestItem

driver = webdriver.Chrome("E:\Warehouse\chromedriver.exe")
driver.get('http://www.quora.com/topic/Job-Interviews/')
SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

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
