import scrapy
#import snoop


class PYTHON_DISTLIB_SPIDER(scrapy.Spider):
    name = 'python_distlib_spider'

    start_urls = ['https://distlib.readthedocs.io']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-distlib'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
