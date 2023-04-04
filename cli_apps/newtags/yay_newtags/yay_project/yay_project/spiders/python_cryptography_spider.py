import scrapy
#import snoop


class PYTHON_CRYPTOGRAPHY_SPIDER(scrapy.Spider):
    name = 'python_cryptography_spider'

    start_urls = ['https://pypi.python.org/pypi/cryptography']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-cryptography'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
