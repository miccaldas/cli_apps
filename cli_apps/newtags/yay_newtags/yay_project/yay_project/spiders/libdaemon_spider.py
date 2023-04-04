import scrapy
#import snoop


class LIBDAEMON_SPIDER(scrapy.Spider):
    name = 'libdaemon_spider'

    start_urls = ['http://0pointer.de/lennart/projects/libdaemon/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libdaemon'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
