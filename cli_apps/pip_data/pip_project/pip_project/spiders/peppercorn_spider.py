import scrapy
#import snoop


class PEPPERCORN_SPIDER(scrapy.Spider):
    name = 'peppercorn_spider'

    start_urls = ['https://docs.pylonsproject.org/projects/peppercorn/en/latest/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'peppercorn'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
