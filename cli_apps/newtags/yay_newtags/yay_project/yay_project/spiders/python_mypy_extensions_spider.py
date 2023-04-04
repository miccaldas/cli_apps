import scrapy
#import snoop


class PYTHON_MYPY_EXTENSIONS_SPIDER(scrapy.Spider):
    name = 'python_mypy_extensions_spider'

    start_urls = ['http://www.mypy-lang.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-mypy_extensions'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
