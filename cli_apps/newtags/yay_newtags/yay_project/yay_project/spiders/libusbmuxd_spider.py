import scrapy
#import snoop


class LIBUSBMUXD_SPIDER(scrapy.Spider):
    name = 'libusbmuxd_spider'

    start_urls = ['https://marcansoft.com/blog/iphonelinux/usbmuxd/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libusbmuxd'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
