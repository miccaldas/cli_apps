import scrapy
#import snoop


class RUBY_GETOPTLONG_SPIDER(scrapy.Spider):
    name = 'ruby_getoptlong_spider'

    start_urls = ['https://github.com/ruby/getoptlong']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'ruby-getoptlong'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
