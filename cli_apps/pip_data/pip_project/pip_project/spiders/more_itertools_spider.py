import scrapy
#import snoop


class MORE_ITERTOOLS_SPIDER(scrapy.Spider):
    name = 'more_itertools_spider'

    start_urls = ['NA']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'more-itertools'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
