import scrapy
#import snoop


class COLORLOG_SPIDER(scrapy.Spider):
    name = 'colorlog_spider'

    start_urls = ['https://github.com/borntyping/python-colorlog']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'colorlog'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
