import scrapy
#import snoop


class PYTHON_LEVENSHTEIN_SPIDER(scrapy.Spider):
    name = 'python_levenshtein_spider'

    start_urls = ['https://pypi.python.org/pypi/python-Levenshtein/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-levenshtein'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
