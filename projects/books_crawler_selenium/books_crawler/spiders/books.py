# -*- coding: utf-8 -*-
from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from time import sleep
from selenium.common.exceptions import NoSuchElementException

class BooksSpider(Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']

    def start_requests(self):
        self.driver =  webdriver.Chrome('E:/Warehouse/chromedriver.exe')
        self.driver.get('http://books.toscrape.com')

        sel = Selector(text = self.driver.page_source)
        books = sel.xpath('//h3/a/@href').extract()
        for book in books:
            url = 'http://books.toscrape.com/'+ book
            yield Request(url, callback = self.parse_book)

        while True:
            try:
                next_page = driver.find_element_by_xpath('//a[text() == "next"]')
                sleep(3)
                self.logger.info('Sleeping for 3 seconds')
                next_page.click()

                sel = Selector(text = self.driver.page_source)
                books = sel.xpath('//h3/a/@href').extract()
                for book in books:
                    url =   'http://books.toscrape.com/' + book
                    yield Request(url, callback = self.parse_book)

            except NoSuchElementException:
                self.logger.info('No more pages to find')
                self.driver.quit()
                break

    def parse_book(self, response):
        pass