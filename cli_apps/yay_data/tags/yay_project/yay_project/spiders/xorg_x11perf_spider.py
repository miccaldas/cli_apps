import scrapy
#import snoop


class XORG_X11PERF_SPIDER(scrapy.Spider):
    name = 'xorg_x11perf_spider'

    start_urls = ['https://github.com/freedesktop/xorg-x11perf']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'xorg-x11perf'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
