import scrapy
#import snoop


class DEBTCOLLECTOR_SPIDER(scrapy.Spider):
    name = 'debtcollector_spider'

    start_urls = ['https://docs.openstack.org/debtcollector/latest']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'debtcollector'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
