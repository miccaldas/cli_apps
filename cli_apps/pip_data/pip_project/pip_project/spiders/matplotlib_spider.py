import scrapy
#import snoop


class MATPLOTLIB_SPIDER(scrapy.Spider):
    name = 'matplotlib_spider'

    start_urls = ['https://matplotlib.org']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'matplotlib'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
