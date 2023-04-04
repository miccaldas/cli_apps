import scrapy
#import snoop


class LIBWPS_SPIDER(scrapy.Spider):
    name = 'libwps_spider'

    start_urls = ['https://sourceforge.net/projects/libwps/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libwps'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
