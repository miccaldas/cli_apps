import scrapy
#import snoop


class PYTHON_ORDERED_SET_SPIDER(scrapy.Spider):
    name = 'python_ordered_set_spider'

    start_urls = ['https://github.com/rspeer/ordered-set']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-ordered-set'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
