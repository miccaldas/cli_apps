import scrapy
#import snoop


class DBFREAD_SPIDER(scrapy.Spider):
    name = 'dbfread_spider'

    start_urls = ['https://dbfread.readthedocs.io/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'dbfread'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
