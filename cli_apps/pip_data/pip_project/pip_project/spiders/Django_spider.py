import scrapy
#import snoop


class DJANGO_SPIDER(scrapy.Spider):
    name = 'Django_spider'

    start_urls = ['https://www.djangoproject.com/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'Django'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
