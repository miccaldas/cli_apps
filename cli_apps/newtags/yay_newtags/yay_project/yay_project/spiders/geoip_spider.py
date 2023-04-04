import scrapy
#import snoop


class GEOIP_SPIDER(scrapy.Spider):
    name = 'geoip_spider'

    start_urls = ['https://www.maxmind.com/app/c']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'geoip'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
