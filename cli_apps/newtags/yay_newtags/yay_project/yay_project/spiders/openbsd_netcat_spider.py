import scrapy
#import snoop


class OPENBSD_NETCAT_SPIDER(scrapy.Spider):
    name = 'openbsd_netcat_spider'

    start_urls = ['https://salsa.debian.org/debian/netcat-openbsd']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'openbsd-netcat'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
