import scrapy
#import snoop


class XORG_UTIL_MACROS_SPIDER(scrapy.Spider):
    name = 'xorg_util_macros_spider'

    start_urls = ['https://github.com/freedesktop/xorg-util-macros']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'xorg-util-macros'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
