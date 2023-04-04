import scrapy
#import snoop


class LIBXSS_SPIDER(scrapy.Spider):
    name = 'libxss_spider'

    start_urls = ['https://gitlab.freedesktop.org/xorg/lib/libxscrnsaver']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libxss'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
