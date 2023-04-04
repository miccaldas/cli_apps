import scrapy
#import snoop


class PYTHON_CRONITER_SPIDER(scrapy.Spider):
    name = 'python_croniter_spider'

    start_urls = ['https://github.com/kiorky/croniter']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-croniter'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
