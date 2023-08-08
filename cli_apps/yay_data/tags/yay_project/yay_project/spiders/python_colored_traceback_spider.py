import scrapy
#import snoop


class PYTHON_COLORED_TRACEBACK_SPIDER(scrapy.Spider):
    name = 'python_colored_traceback_spider'

    start_urls = ['https://github.com/staticshock/colored-traceback.py']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-colored-traceback'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
