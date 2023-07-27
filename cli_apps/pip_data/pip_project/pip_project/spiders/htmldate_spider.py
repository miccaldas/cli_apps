import scrapy
#import snoop


class HTMLDATE_SPIDER(scrapy.Spider):
    name = 'htmldate_spider'

    start_urls = ['https://htmldate.readthedocs.io']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'htmldate'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
