import scrapy
#import snoop


class BC_SPIDER(scrapy.Spider):
    name = 'bc_spider'

    start_urls = ['https://www.gnu.org/software/bc/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'bc'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
