import scrapy
#import snoop


class FIRE_SPIDER(scrapy.Spider):
    name = 'fire_spider'

    start_urls = ['https://github.com/google/python-fire']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'fire'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
