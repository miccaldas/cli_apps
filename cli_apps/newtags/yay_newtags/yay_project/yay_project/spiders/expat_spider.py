import scrapy
#import snoop


class EXPAT_SPIDER(scrapy.Spider):
    name = 'expat_spider'

    start_urls = ['https://libexpat.github.io/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'expat'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
