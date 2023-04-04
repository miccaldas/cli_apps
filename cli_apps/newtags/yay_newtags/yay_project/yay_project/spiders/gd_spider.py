import scrapy
#import snoop


class GD_SPIDER(scrapy.Spider):
    name = 'gd_spider'

    start_urls = ['https://libgd.github.io/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'gd'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
