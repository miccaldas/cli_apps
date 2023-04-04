import scrapy
#import snoop


class SIGNOND_SPIDER(scrapy.Spider):
    name = 'signond_spider'

    start_urls = ['https://gitlab.com/accounts-sso/signond/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'signond'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
