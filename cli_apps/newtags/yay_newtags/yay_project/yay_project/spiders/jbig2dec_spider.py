import scrapy
#import snoop


class JBIG2DEC_SPIDER(scrapy.Spider):
    name = 'jbig2dec_spider'

    start_urls = ['https://jbig2dec.com/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'jbig2dec'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
