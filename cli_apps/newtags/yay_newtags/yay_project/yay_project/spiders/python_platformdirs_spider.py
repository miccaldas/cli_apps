import scrapy
#import snoop


class PYTHON_PLATFORMDIRS_SPIDER(scrapy.Spider):
    name = 'python_platformdirs_spider'

    start_urls = ['https://github.com/platformdirs/platformdirs']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-platformdirs'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
