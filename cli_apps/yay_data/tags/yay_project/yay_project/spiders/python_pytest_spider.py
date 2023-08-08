import scrapy
#import snoop


class PYTHON_PYTEST_SPIDER(scrapy.Spider):
    name = 'python_pytest_spider'

    start_urls = ['https://pytest.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-pytest'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
