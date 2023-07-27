import scrapy
#import snoop


class FLASK_HUMANIZE_SPIDER(scrapy.Spider):
    name = 'Flask_Humanize_spider'

    start_urls = ['https://github.com/vitalk/flask-humanize']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'Flask-Humanize'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
