import scrapy
#import snoop


class SPHINX_BASIC_NG_SPIDER(scrapy.Spider):
    name = 'sphinx_basic_ng_spider'

    start_urls = ['https://github.com/pradyunsg/sphinx-basic-ng']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'sphinx-basic-ng'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
