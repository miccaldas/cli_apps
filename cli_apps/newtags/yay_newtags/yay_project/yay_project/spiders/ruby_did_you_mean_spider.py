import scrapy
#import snoop


class RUBY_DID_YOU_MEAN_SPIDER(scrapy.Spider):
    name = 'ruby_did_you_mean_spider'

    start_urls = ['https://github.com/ruby/did_you_mean']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'ruby-did_you_mean'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
