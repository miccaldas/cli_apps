import scrapy
#import snoop


class MAILCAP_SPIDER(scrapy.Spider):
    name = 'mailcap_spider'

    start_urls = ['https://pagure.io/mailcap']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'mailcap'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
