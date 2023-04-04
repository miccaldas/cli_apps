import scrapy
#import snoop


class OSINFO_DB_SPIDER(scrapy.Spider):
    name = 'osinfo_db_spider'

    start_urls = ['https://libosinfo.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'osinfo-db'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
