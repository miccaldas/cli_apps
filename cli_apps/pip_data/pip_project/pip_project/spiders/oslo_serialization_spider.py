import scrapy
#import snoop


class OSLO_SERIALIZATION_SPIDER(scrapy.Spider):
    name = 'oslo_serialization_spider'

    start_urls = ['https://docs.openstack.org/oslo.serialization/latest/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'oslo.serialization'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
