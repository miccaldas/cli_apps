import scrapy
#import snoop


class RUBY_MINITEST_SPIDER(scrapy.Spider):
    name = 'ruby_minitest_spider'

    start_urls = ['https://github.com/seattlerb/minitest']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'ruby-minitest'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
