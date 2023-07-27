import scrapy
#import snoop


class JINJA2_SPIDER(scrapy.Spider):
    name = 'Jinja2_spider'

    start_urls = ['https://palletsprojects.com/p/jinja/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'Jinja2'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
