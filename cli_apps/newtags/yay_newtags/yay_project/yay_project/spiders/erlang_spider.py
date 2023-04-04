import scrapy
#import snoop


class ERLANG_SPIDER(scrapy.Spider):
    name = 'erlang_spider'

    start_urls = ['https://erlang.org']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'erlang'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
