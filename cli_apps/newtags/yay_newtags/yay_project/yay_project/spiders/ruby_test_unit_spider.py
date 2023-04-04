import scrapy
#import snoop


class RUBY_TEST_UNIT_SPIDER(scrapy.Spider):
    name = 'ruby_test_unit_spider'

    start_urls = ['https://github.com/test-unit/test-unit']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'ruby-test-unit'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
