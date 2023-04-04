import scrapy
#import snoop


class READLINE_SPIDER(scrapy.Spider):
    name = 'readline_spider'

    start_urls = ['https://tiswww.case.edu/php/chet/readline/rltop.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'readline'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
