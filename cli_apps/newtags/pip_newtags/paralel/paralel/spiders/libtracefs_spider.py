import scrapy
#import snoop


class LIBTRACEFS_SPIDER(scrapy.Spider):
    name = 'libtracefs_spider'

    start_urls = ['https://github.com/rostedt/libtracefs']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libtracefs'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
