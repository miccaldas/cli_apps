import scrapy
#import snoop


class FD_SPIDER(scrapy.Spider):
    name = 'fd_spider'

    start_urls = ['https://github.com/sharkdp/fd']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'fd'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
