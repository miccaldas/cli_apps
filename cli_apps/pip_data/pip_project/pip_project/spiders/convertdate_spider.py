import scrapy
#import snoop


class CONVERTDATE_SPIDER(scrapy.Spider):
    name = 'convertdate_spider'

    start_urls = ['https://github.com/fitnr/convertdate']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'convertdate'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
