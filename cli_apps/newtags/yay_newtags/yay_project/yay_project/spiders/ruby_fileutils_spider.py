import scrapy
#import snoop


class RUBY_FILEUTILS_SPIDER(scrapy.Spider):
    name = 'ruby_fileutils_spider'

    start_urls = ['https://github.com/ruby/fileutils']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'ruby-fileutils'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
