import scrapy
#import snoop


class PYTHON_CAIRO_SPIDER(scrapy.Spider):
    name = 'python_cairo_spider'

    start_urls = ['https://pycairo.readthedocs.io/en/latest/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-cairo'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
