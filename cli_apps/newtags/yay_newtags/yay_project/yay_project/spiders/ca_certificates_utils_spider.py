import scrapy
#import snoop


class CA_CERTIFICATES_UTILS_SPIDER(scrapy.Spider):
    name = 'ca_certificates_utils_spider'

    start_urls = ['https://src.fedoraproject.org/rpms/ca-certificates']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'ca-certificates-utils'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
