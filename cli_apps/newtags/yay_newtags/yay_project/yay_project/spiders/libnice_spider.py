import scrapy
#import snoop


class LIBNICE_SPIDER(scrapy.Spider):
    name = 'libnice_spider'

    start_urls = ['https://nice.freedesktop.org']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libnice'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
