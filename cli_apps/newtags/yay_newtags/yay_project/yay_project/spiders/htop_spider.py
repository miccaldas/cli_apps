import scrapy
#import snoop


class HTOP_SPIDER(scrapy.Spider):
    name = 'htop_spider'

    start_urls = ['https://htop.dev/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'htop'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
