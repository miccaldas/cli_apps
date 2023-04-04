import scrapy
#import snoop


class LIBP11_KIT_SPIDER(scrapy.Spider):
    name = 'libp11_kit_spider'

    start_urls = ['https://p11-glue.freedesktop.org']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libp11-kit'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
