import scrapy
#import snoop


class LIBXKBCOMMON_X11_SPIDER(scrapy.Spider):
    name = 'libxkbcommon_x11_spider'

    start_urls = ['https://xkbcommon.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libxkbcommon-x11'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
