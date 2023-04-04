import scrapy
#import snoop


class LIBBS2B_SPIDER(scrapy.Spider):
    name = 'libbs2b_spider'

    start_urls = ['http://bs2b.sourceforge.net']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libbs2b'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
