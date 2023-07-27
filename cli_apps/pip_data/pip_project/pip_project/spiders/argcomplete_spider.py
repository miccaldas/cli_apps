import scrapy
#import snoop


class ARGCOMPLETE_SPIDER(scrapy.Spider):
    name = 'argcomplete_spider'

    start_urls = ['https://github.com/kislyuk/argcomplete']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'argcomplete'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
