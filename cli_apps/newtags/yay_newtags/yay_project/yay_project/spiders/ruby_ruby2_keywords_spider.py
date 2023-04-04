import scrapy
#import snoop


class RUBY_RUBY2_KEYWORDS_SPIDER(scrapy.Spider):
    name = 'ruby_ruby2_keywords_spider'

    start_urls = ['https://github.com/ruby/ruby2_keywords']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'ruby-ruby2_keywords'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
