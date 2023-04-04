import scrapy
#import snoop


class EXPECT_SPIDER(scrapy.Spider):
    name = 'expect_spider'

    start_urls = ['https://www.nist.gov/el/msid/expect.cfm']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'expect'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
