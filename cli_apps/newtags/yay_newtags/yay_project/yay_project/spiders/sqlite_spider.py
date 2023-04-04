import scrapy
#import snoop


class SQLITE_SPIDER(scrapy.Spider):
    name = 'sqlite_spider'

    start_urls = ['https://www.sqlite.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'sqlite'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
