import scrapy
#import snoop


class ISORT_SPIDER(scrapy.Spider):
    name = 'isort_spider'

    start_urls = ['https://pycqa.github.io/isort/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'isort'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
