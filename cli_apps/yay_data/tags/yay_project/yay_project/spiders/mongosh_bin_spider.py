import scrapy
#import snoop


class MONGOSH_BIN_SPIDER(scrapy.Spider):
    name = 'mongosh_bin_spider'

    start_urls = ['https://github.com/mongodb-js/mongosh.git']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'mongosh-bin'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
