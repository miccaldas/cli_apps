import scrapy
#import snoop


class PEP517_SPIDER(scrapy.Spider):
    name = 'pep517_spider'

    start_urls = ['https://github.com/pypa/pep517']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'pep517'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
