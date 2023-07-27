import scrapy
#import snoop


class BILLIARD_SPIDER(scrapy.Spider):
    name = 'billiard_spider'

    start_urls = ['https://github.com/celery/billiard']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'billiard'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
