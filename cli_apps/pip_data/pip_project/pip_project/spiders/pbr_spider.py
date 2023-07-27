import scrapy
#import snoop


class PBR_SPIDER(scrapy.Spider):
    name = 'pbr_spider'

    start_urls = ['https://docs.openstack.org/pbr/latest/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'pbr'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
