import scrapy
#import snoop


class SEMVER_SPIDER(scrapy.Spider):
    name = 'semver_spider'

    start_urls = ['https://github.com/npm/node-semver']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'semver'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
