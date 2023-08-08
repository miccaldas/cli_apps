import scrapy
#import snoop


class PYTHON_MANHOLE_SPIDER(scrapy.Spider):
    name = 'python_manhole_spider'

    start_urls = ['https://github.com/ionelmc/python-manhole']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-manhole'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
