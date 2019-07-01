import scrapy
from ..items import NinenineacresItem

class Acres99Spider(scrapy.Spider):
    name = 'acres99'
    allowed_domains = ['www.99acres.com/search/property/buy/residential-all/ghaziabad?search_type=QS&refSection=GNB&search_location=CP20&lstAcn=CP_R&lstAcnId=20&src=CLUSTER&preference=S&selected_tab=1&city=9&res_com=R&property_type=R&isvoicesearch=N&keyword=ghaziabad&strEntityMap=IiI%3D&refine_results=Y&Refine_Localities=Refine%20Localities&action=%2Fdo%2Fquicksearch%2Fsearch&searchform=1&price_min=null&price_max=null']
    start_urls = ['http://www.99acres.com/search/property/buy/residential-all/ghaziabad?search_type=QS&refSection=GNB&search_location=CP20&lstAcn=CP_R&lstAcnId=20&src=CLUSTER&preference=S&selected_tab=1&city=9&res_com=R&property_type=R&isvoicesearch=N&keyword=ghaziabad&strEntityMap=IiI%3D&refine_results=Y&Refine_Localities=Refine%20Localities&action=%2Fdo%2Fquicksearch%2Fsearch&searchform=1&price_min=null&price_max=null/']

    def parse(self, response):
        nextpageurl = response.xpath('//*[@class = "pgselActive"]/@href')

        for item in self.scrape(response):
            yield item

        if nextpageurl:
            path = nextpageurl.extract_first()
            # nextpage = "http://www.99acres.com" + path
            nextpage = response.urljoin(path)
            print("Found url: {}".format(nextpage))
            yield scrapy.Request(nextpage, callback=self.parse)

    def scrape(self, response):
        title = response.xpath('//*[@class = "srpNw_tble "]/table/tbody/tr/th/a/span/text()').extract()
        location = response.xpath('//*[@class = "srpNw_tble "]/table/tbody/tr/th/a/span/b/text()').extract()
        price = response.xpath('//*[@class = "srpNw_price "]/text()').extract()
        area = response.xpath('//*[@class = "_auto_areaValue"]/b/text()').extract()
        bhks = response.xpath('//*[@class = "_auto_bedroom"]/b/text()').extract()
        bath_bal = response.xpath('//*[@class = "_auto_bath_balc_roadText"]/text()').extract()


        for items in zip(title, location, price, area, bhks, bath_bal):
            new_item = NinenineacresItem()

            new_item['title'] = items[0]
            new_item['location'] = items[1]
            new_item['price'] = items[2]
            new_item['area'] = items[3]
            new_item['bhks'] = items[4]
            new_item['bath_bal'] = items[5]

            yield new_item
