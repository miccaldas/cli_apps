import scrapy
#import snoop


class JQ_SPIDER(scrapy.Spider):
    name = 'jq_spider'

    start_urls = ['https://stedolan.github.io/jq/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'jq'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
