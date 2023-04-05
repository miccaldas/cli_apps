import scrapy
#import snoop


class PYAHOCORASICK_SPIDER(scrapy.Spider):
    name = 'pyahocorasick_spider'

    start_urls = ['http://github.com/WojciechMula/pyahocorasick']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'pyahocorasick'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
