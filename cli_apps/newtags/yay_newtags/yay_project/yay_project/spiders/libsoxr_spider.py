import scrapy
#import snoop


class LIBSOXR_SPIDER(scrapy.Spider):
    name = 'libsoxr_spider'

    start_urls = ['https://sourceforge.net/p/soxr/wiki/Home/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libsoxr'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
