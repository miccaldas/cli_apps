import scrapy
#import snoop


class TYPING_SPIDER(scrapy.Spider):
    name = 'typing_spider'

    start_urls = ['https://docs.python.org/3/library/typing.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'typing'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
