import scrapy
#import snoop


class XORG_XREFRESH_SPIDER(scrapy.Spider):
    name = 'xorg_xrefresh_spider'

    start_urls = ['https://github.com/freedesktop/xorg-xrefresh']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'xorg-xrefresh'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
