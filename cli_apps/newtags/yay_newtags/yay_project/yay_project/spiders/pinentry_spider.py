import scrapy
#import snoop


class PINENTRY_SPIDER(scrapy.Spider):
    name = 'pinentry_spider'

    start_urls = ['https://gnupg.org/related_software/pinentry/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'pinentry'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
