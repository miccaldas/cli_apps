import scrapy
#import snoop


class PIP_SPIDER(scrapy.Spider):
    name = 'pip_spider'

    start_urls = ['https://pip.pypa.io/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'pip'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
