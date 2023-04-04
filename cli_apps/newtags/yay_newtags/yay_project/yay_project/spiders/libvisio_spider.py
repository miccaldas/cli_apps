import scrapy
#import snoop


class LIBVISIO_SPIDER(scrapy.Spider):
    name = 'libvisio_spider'

    start_urls = ['https://wiki.documentfoundation.org/DLP/Libraries/libvisio']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libvisio'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
