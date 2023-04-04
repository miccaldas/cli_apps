import scrapy
#import snoop


class RUBY_IRB_SPIDER(scrapy.Spider):
    name = 'ruby_irb_spider'

    start_urls = ['https://github.com/ruby/irb']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'ruby-irb'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
