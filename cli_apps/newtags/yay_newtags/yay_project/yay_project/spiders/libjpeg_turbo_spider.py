import scrapy
#import snoop


class LIBJPEG_TURBO_SPIDER(scrapy.Spider):
    name = 'libjpeg_turbo_spider'

    start_urls = ['https://libjpeg-turbo.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libjpeg-turbo'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
