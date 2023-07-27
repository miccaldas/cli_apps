import scrapy
#import snoop


class CLICK_REPL_SPIDER(scrapy.Spider):
    name = 'click_repl_spider'

    start_urls = ['https://github.com/untitaker/click-repl']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'click-repl'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
