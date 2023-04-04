import scrapy
#import snoop


class TZDATA_SPIDER(scrapy.Spider):
    name = 'tzdata_spider'

    start_urls = ['https://www.iana.org/time-zones']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'tzdata'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
