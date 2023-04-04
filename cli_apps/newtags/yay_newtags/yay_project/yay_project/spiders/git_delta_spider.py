import scrapy
#import snoop


class GIT_DELTA_SPIDER(scrapy.Spider):
    name = 'git_delta_spider'

    start_urls = ['https://github.com/dandavison/delta']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'git-delta'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
