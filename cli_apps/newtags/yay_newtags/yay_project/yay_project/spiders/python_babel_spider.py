import scrapy
#import snoop


class PYTHON_BABEL_SPIDER(scrapy.Spider):
    name = 'python_babel_spider'

    start_urls = ['http://babel.pocoo.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-babel'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
