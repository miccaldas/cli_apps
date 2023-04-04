import scrapy
#import snoop


class PYTHON_CONTEXTLIB2_SPIDER(scrapy.Spider):
    name = 'python_contextlib2_spider'

    start_urls = ['https://github.com/jazzband/contextlib2']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-contextlib2'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
