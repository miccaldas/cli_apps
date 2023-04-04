import scrapy
#import snoop


class CA_CERTIFICATES_MOZILLA_SPIDER(scrapy.Spider):
    name = 'ca_certificates_mozilla_spider'

    start_urls = ['https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'ca-certificates-mozilla'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
