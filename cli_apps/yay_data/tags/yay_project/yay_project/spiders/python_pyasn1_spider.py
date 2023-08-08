import scrapy
#import snoop


class PYTHON_PYASN1_SPIDER(scrapy.Spider):
    name = 'python_pyasn1_spider'

    start_urls = ['https://github.com/etingof/pyasn1']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-pyasn1'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
