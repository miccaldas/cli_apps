import scrapy
#import snoop


class INFLECT_SPIDER(scrapy.Spider):
    name = 'inflect_spider'

    start_urls = ['https://github.com/jaraco/inflect']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'inflect'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
