import scrapy
#import snoop


class RUBY_BIGDECIMAL_SPIDER(scrapy.Spider):
    name = 'ruby_bigdecimal_spider'

    start_urls = ['https://github.com/ruby/bigdecimal']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'ruby-bigdecimal'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results