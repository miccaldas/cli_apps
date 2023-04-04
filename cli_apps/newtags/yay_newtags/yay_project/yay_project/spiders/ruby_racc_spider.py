import scrapy
#import snoop


class RUBY_RACC_SPIDER(scrapy.Spider):
    name = 'ruby_racc_spider'

    start_urls = ['https://github.com/ruby/racc']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'ruby-racc'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
