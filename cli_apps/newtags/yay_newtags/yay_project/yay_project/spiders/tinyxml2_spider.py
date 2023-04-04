import scrapy
#import snoop


class TINYXML2_SPIDER(scrapy.Spider):
    name = 'tinyxml2_spider'

    start_urls = ['http://www.grinninglizard.com/tinyxml2']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'tinyxml2'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
