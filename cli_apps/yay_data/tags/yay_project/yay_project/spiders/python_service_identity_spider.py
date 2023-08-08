import scrapy
#import snoop


class PYTHON_SERVICE_IDENTITY_SPIDER(scrapy.Spider):
    name = 'python_service_identity_spider'

    start_urls = ['https://pypi.python.org/pypi/service_identity']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-service-identity'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
