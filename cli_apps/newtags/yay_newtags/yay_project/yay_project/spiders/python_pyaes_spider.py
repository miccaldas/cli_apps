import scrapy
#import snoop


class PYTHON_PYAES_SPIDER(scrapy.Spider):
    name = 'python_pyaes_spider'

    start_urls = ['https://github.com/ricmoo/pyaes']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-pyaes'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
