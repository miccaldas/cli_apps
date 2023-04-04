import scrapy
#import snoop


class DAV1D_SPIDER(scrapy.Spider):
    name = 'dav1d_spider'

    start_urls = ['https://code.videolan.org/videolan/dav1d/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'dav1d'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
