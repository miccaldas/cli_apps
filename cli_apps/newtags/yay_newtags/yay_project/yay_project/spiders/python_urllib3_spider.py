import scrapy
#import snoop


class PYTHON_URLLIB3_SPIDER(scrapy.Spider):
    name = 'python_urllib3_spider'

    start_urls = ['https://github.com/urllib3/urllib3']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-urllib3'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
