import scrapy
#import snoop


class RUBY_RAKE_SPIDER(scrapy.Spider):
    name = 'ruby_rake_spider'

    start_urls = ['https://ruby.github.io/rake/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'ruby-rake'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
