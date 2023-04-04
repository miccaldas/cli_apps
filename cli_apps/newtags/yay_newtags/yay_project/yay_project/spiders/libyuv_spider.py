import scrapy
#import snoop


class LIBYUV_SPIDER(scrapy.Spider):
    name = 'libyuv_spider'

    start_urls = ['https://chromium.googlesource.com/libyuv/libyuv/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libyuv'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
