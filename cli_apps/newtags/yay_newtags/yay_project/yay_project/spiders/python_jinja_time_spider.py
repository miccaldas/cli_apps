import scrapy
#import snoop


class PYTHON_JINJA_TIME_SPIDER(scrapy.Spider):
    name = 'python_jinja_time_spider'

    start_urls = ['https://github.com/hackebrot/jinja2-time']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-jinja-time'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
