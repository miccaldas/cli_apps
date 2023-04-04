import scrapy
#import snoop


class PYTHON_VALIDATE_PYPROJECT_SPIDER(scrapy.Spider):
    name = 'python_validate_pyproject_spider'

    start_urls = ['https://github.com/abravalheri/validate-pyproject']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-validate-pyproject'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
