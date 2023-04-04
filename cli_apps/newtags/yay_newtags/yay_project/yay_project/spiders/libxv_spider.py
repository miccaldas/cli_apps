import scrapy
#import snoop


class LIBXV_SPIDER(scrapy.Spider):
    name = 'libxv_spider'

    start_urls = ['https://github.com/freedesktop/xorg-libxv']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libxv'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
