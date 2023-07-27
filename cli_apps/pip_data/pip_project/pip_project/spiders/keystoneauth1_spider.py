import scrapy
#import snoop


class KEYSTONEAUTH1_SPIDER(scrapy.Spider):
    name = 'keystoneauth1_spider'

    start_urls = ['https://docs.openstack.org/keystoneauth/latest/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'keystoneauth1'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
