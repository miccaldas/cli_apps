import scrapy
#import snoop


class RUBY_MUTEX_M_SPIDER(scrapy.Spider):
    name = 'ruby_mutex_m_spider'

    start_urls = ['https://github.com/ruby/mutex_m']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'ruby-mutex_m'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
