import scrapy
#import snoop


class MPG123_SPIDER(scrapy.Spider):
    name = 'mpg123_spider'

    start_urls = ['https://sourceforge.net/projects/mpg123']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'mpg123'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
