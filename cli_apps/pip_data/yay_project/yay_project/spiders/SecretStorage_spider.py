import scrapy
#import snoop


class SECRETSTORAGE_SPIDER(scrapy.Spider):
    name = 'SecretStorage_spider'

    start_urls = ['https://github.com/mitya57/secretstorage']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'SecretStorage'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
