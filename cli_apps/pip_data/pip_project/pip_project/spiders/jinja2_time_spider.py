import scrapy
#import snoop


class JINJA2_TIME_SPIDER(scrapy.Spider):
    name = 'jinja2_time_spider'

    start_urls = ['https://github.com/hackebrot/jinja2-time']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'jinja2-time'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
