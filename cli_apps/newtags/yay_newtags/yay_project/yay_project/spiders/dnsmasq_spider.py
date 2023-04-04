import scrapy
#import snoop


class DNSMASQ_SPIDER(scrapy.Spider):
    name = 'dnsmasq_spider'

    start_urls = ['http://www.thekelleys.org.uk/dnsmasq/doc.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'dnsmasq'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
