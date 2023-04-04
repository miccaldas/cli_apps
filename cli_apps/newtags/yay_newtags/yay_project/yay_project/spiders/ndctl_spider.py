import scrapy
#import snoop


class NDCTL_SPIDER(scrapy.Spider):
    name = 'ndctl_spider'

    start_urls = ['https://github.com/pmem/ndctl']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'ndctl'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
