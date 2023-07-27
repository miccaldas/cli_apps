import scrapy
#import snoop


class PRIORITY_SPIDER(scrapy.Spider):
    name = 'priority_spider'

    start_urls = ['https://github.com/python-hyper/priority/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'priority'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
