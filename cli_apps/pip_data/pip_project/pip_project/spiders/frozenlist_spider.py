import scrapy
#import snoop


class FROZENLIST_SPIDER(scrapy.Spider):
    name = 'frozenlist_spider'

    start_urls = ['https://github.com/aio-libs/frozenlist']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'frozenlist'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
