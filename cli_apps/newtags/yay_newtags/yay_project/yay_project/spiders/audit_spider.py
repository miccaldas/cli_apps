import scrapy
#import snoop


class AUDIT_SPIDER(scrapy.Spider):
    name = 'audit_spider'

    start_urls = ['https://people.redhat.com/sgrubb/audit']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'audit'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
