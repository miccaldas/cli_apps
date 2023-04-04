import scrapy
#import snoop


class LIBMFX_SPIDER(scrapy.Spider):
    name = 'libmfx_spider'

    start_urls = ['https://software.intel.com/en-us/media-sdk/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libmfx'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
