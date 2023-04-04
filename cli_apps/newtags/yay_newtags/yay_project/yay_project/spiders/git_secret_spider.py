import scrapy
#import snoop


class GIT_SECRET_SPIDER(scrapy.Spider):
    name = 'git_secret_spider'

    start_urls = ['https://github.com/sobolevn/git-secret/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'git-secret'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
