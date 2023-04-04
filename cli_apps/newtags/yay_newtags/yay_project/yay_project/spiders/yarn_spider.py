import scrapy
#import snoop


class YARN_SPIDER(scrapy.Spider):
    name = 'yarn_spider'

    start_urls = ['https://classic.yarnpkg.com/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'yarn'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
