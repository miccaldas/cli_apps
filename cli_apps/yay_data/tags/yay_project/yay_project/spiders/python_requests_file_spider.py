import scrapy
#import snoop


class PYTHON_REQUESTS_FILE_SPIDER(scrapy.Spider):
    name = 'python_requests_file_spider'

    start_urls = ['https://github.com/dashea/requests-file']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-requests-file'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
