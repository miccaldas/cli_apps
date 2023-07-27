import scrapy
#import snoop


class PLASTER_SPIDER(scrapy.Spider):
    name = 'plaster_spider'

    start_urls = ['https://docs.pylonsproject.org/projects/plaster/en/latest/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'plaster'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
