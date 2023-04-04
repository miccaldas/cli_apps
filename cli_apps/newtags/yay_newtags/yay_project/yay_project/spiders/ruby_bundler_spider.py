import scrapy
#import snoop


class RUBY_BUNDLER_SPIDER(scrapy.Spider):
    name = 'ruby_bundler_spider'

    start_urls = ['https://bundler.io']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'ruby-bundler'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
