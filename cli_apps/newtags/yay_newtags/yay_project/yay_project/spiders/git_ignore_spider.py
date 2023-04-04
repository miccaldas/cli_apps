import scrapy
#import snoop


class GIT_IGNORE_SPIDER(scrapy.Spider):
    name = 'git_ignore_spider'

    start_urls = ['https://github.com/sondr3/git-ignore']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'git-ignore'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
