import scrapy
#import snoop


class PYTHON_SETUPTOOLS_SPIDER(scrapy.Spider):
    name = 'python_setuptools_spider'

    start_urls = ['https://pypi.org/project/setuptools/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-setuptools'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
