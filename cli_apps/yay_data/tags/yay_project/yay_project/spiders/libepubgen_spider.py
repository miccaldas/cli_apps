import scrapy
#import snoop


class LIBEPUBGEN_SPIDER(scrapy.Spider):
    name = 'libepubgen_spider'

    start_urls = ['https://sourceforge.net/projects/libepubgen/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libepubgen'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
