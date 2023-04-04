import scrapy
#import snoop


class REDLAND_SPIDER(scrapy.Spider):
    name = 'redland_spider'

    start_urls = ['http://librdf.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'redland'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
