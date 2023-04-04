import scrapy
#import snoop


class LIBABW_SPIDER(scrapy.Spider):
    name = 'libabw_spider'

    start_urls = ['https://wiki.documentfoundation.org/DLP/Libraries/libabw']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libabw'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
