import scrapy
#import snoop


class FEEDFINDER2_SPIDER(scrapy.Spider):
    name = 'feedfinder2_spider'

    start_urls = ['https://github.com/dfm/feedfinder2']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'feedfinder2'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
