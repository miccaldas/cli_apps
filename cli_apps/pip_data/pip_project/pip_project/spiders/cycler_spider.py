import scrapy
#import snoop


class CYCLER_SPIDER(scrapy.Spider):
    name = 'cycler_spider'

    start_urls = ['https://github.com/matplotlib/cycler']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'cycler'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
