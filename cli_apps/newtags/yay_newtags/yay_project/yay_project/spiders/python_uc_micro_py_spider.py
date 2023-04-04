import scrapy
#import snoop


class PYTHON_UC_MICRO_PY_SPIDER(scrapy.Spider):
    name = 'python_uc_micro_py_spider'

    start_urls = ['https://github.com/tsutsu3/uc.micro-py']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-uc-micro-py'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
