import scrapy
#import snoop


class PLOTLY_SPIDER(scrapy.Spider):
    name = 'plotly_spider'

    start_urls = ['https://plotly.com/python/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'plotly'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
