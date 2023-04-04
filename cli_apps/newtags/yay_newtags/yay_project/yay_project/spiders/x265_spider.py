import scrapy
#import snoop


class X265_SPIDER(scrapy.Spider):
    name = 'x265_spider'

    start_urls = ['https://bitbucket.org/multicoreware/x265_git']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'x265'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
