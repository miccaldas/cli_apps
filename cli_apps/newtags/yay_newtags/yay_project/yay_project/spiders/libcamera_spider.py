import scrapy
#import snoop


class LIBCAMERA_SPIDER(scrapy.Spider):
    name = 'libcamera_spider'

    start_urls = ['https://libcamera.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libcamera'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
