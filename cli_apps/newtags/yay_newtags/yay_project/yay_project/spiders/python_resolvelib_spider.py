import scrapy
#import snoop


class PYTHON_RESOLVELIB_SPIDER(scrapy.Spider):
    name = 'python_resolvelib_spider'

    start_urls = ['https://github.com/sarugaku/resolvelib']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-resolvelib'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
