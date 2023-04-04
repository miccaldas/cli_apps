import scrapy
#import snoop


class IANA_ETC_SPIDER(scrapy.Spider):
    name = 'iana_etc_spider'

    start_urls = ['https://www.iana.org/protocols']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'iana-etc'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
