import scrapy
#import snoop


class W3M_SPIDER(scrapy.Spider):
    name = 'w3m_spider'

    start_urls = ['https://salsa.debian.org/debian/w3m']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'w3m'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
