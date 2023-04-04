import scrapy
#import snoop


class LIBMSPACK_SPIDER(scrapy.Spider):
    name = 'libmspack_spider'

    start_urls = ['https://www.cabextract.org.uk/libmspack/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libmspack'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
