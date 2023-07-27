import scrapy
#import snoop


class CSVKIT_SPIDER(scrapy.Spider):
    name = 'csvkit_spider'

    start_urls = ['https://github.com/wireservice/csvkit']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'csvkit'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
