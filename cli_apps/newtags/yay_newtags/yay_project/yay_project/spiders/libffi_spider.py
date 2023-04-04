import scrapy
#import snoop


class LIBFFI_SPIDER(scrapy.Spider):
    name = 'libffi_spider'

    start_urls = ['https://sourceware.org/libffi/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libffi'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
