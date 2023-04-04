import scrapy
#import snoop


class SNAPPY_SPIDER(scrapy.Spider):
    name = 'snappy_spider'

    start_urls = ['https://google.github.io/snappy/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'snappy'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
