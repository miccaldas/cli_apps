import scrapy
#import snoop


class FLAC_SPIDER(scrapy.Spider):
    name = 'flac_spider'

    start_urls = ['https://xiph.org/flac/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'flac'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
