import scrapy
#import snoop


class LIBX11_SPIDER(scrapy.Spider):
    name = 'libx11_spider'

    start_urls = ['https://github.com/freedesktop/xorg-libx11']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libx11'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
