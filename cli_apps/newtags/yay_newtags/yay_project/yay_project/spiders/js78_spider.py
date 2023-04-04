import scrapy
#import snoop


class JS78_SPIDER(scrapy.Spider):
    name = 'js78_spider'

    start_urls = ['https://spidermonkey.dev/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'js78'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
