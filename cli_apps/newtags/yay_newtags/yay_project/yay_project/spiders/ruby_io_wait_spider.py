import scrapy
#import snoop


class RUBY_IO_WAIT_SPIDER(scrapy.Spider):
    name = 'ruby_io_wait_spider'

    start_urls = ['https://github.com/ruby/io-wait']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'ruby-io-wait'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
