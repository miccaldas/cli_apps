import scrapy
#import snoop


class NODE_GYP_SPIDER(scrapy.Spider):
    name = 'node_gyp_spider'

    start_urls = ['https://github.com/nodejs/node-gyp']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'node-gyp'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
