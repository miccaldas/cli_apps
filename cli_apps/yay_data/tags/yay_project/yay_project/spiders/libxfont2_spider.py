import scrapy
#import snoop


class LIBXFONT2_SPIDER(scrapy.Spider):
    name = 'libxfont2_spider'

    start_urls = ['https://github.com/freedesktop/xorg-libxfont2']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libxfont2'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
