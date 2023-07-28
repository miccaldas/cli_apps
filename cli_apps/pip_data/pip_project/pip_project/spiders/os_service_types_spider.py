import scrapy
#import snoop


class OS_SERVICE_TYPES_SPIDER(scrapy.Spider):
    name = 'os_service_types_spider'

    start_urls = ['https://docs.openstack.org/os-service-types/latest/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'os-service-types'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results