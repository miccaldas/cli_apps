import scrapy
#import snoop


class NEWSPAPER3K_SPIDER(scrapy.Spider):
    name = 'newspaper3k_spider'

    start_urls = ['https://github.com/codelucas/newspaper/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'newspaper3k'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
