import scrapy
#import snoop


class PIP_SEARCH_SPIDER(scrapy.Spider):
    name = 'pip_search_spider'

    start_urls = ['https://github.com/victorgarric/pip_search']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'pip-search'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
