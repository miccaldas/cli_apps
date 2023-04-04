import scrapy
#import snoop


class RUBY_RDOC_SPIDER(scrapy.Spider):
    name = 'ruby_rdoc_spider'

    start_urls = ['https://ruby.github.io/rdoc/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'ruby-rdoc'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
