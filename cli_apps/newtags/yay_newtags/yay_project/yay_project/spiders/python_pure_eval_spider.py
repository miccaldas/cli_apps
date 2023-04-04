import scrapy
#import snoop


class PYTHON_PURE_EVAL_SPIDER(scrapy.Spider):
    name = 'python_pure_eval_spider'

    start_urls = ['https://github.com/alexmojaki/pure_eval']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-pure-eval'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
