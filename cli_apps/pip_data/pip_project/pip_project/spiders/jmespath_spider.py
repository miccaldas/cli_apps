import scrapy
#import snoop


class JMESPATH_SPIDER(scrapy.Spider):
    name = 'jmespath_spider'

    start_urls = ['https://github.com/jmespath/jmespath.py']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'jmespath'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
