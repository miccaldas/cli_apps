import scrapy
#import snoop


class RAPTOR_SPIDER(scrapy.Spider):
    name = 'raptor_spider'

    start_urls = ['https://librdf.org/raptor']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'raptor'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
