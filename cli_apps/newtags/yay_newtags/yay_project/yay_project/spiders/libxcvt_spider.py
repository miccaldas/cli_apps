import scrapy
#import snoop


class LIBXCVT_SPIDER(scrapy.Spider):
    name = 'libxcvt_spider'

    start_urls = ['https://gitlab.freedesktop.org/xorg/lib/libxcvt']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libxcvt'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
