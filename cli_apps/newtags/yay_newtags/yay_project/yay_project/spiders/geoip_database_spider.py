import scrapy
#import snoop


class GEOIP_DATABASE_SPIDER(scrapy.Spider):
    name = 'geoip_database_spider'

    start_urls = ['https://mailfud.org/geoip-legacy/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'geoip-database'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
