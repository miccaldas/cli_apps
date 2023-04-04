import scrapy
#import snoop


class XCB_UTIL_CURSOR_SPIDER(scrapy.Spider):
    name = 'xcb_util_cursor_spider'

    start_urls = ['https://cgit.freedesktop.org/xcb/util-cursor']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'xcb-util-cursor'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
