import scrapy
#import snoop


class IPYTHON_SPIDER(scrapy.Spider):
    name = 'ipython_spider'

    start_urls = ['https://ipython.org']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'ipython'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
