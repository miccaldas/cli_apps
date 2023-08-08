import scrapy
#import snoop


class XORG_XDPYINFO_SPIDER(scrapy.Spider):
    name = 'xorg_xdpyinfo_spider'

    start_urls = ['https://github.com/freedesktop/xorg-xdpyinfo']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'xorg-xdpyinfo'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
