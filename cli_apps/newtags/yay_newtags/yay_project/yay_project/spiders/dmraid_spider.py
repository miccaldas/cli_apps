import scrapy
#import snoop


class DMRAID_SPIDER(scrapy.Spider):
    name = 'dmraid_spider'

    start_urls = ['https://people.redhat.com/~heinzm/sw/dmraid/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'dmraid'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
