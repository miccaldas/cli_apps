import scrapy
#import snoop


class LIBIMOBILEDEVICE_SPIDER(scrapy.Spider):
    name = 'libimobiledevice_spider'

    start_urls = ['https://libimobiledevice.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libimobiledevice'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
