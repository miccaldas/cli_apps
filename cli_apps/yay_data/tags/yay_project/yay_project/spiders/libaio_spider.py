import scrapy
#import snoop


class LIBAIO_SPIDER(scrapy.Spider):
    name = 'libaio_spider'

    start_urls = ['https://pagure.io/libaio']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libaio'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
