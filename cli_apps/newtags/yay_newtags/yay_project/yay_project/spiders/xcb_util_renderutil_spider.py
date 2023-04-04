import scrapy
#import snoop


class XCB_UTIL_RENDERUTIL_SPIDER(scrapy.Spider):
    name = 'xcb_util_renderutil_spider'

    start_urls = ['https://xcb.freedesktop.org']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'xcb-util-renderutil'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
