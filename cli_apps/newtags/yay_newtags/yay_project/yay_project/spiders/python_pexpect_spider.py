import scrapy
#import snoop


class PYTHON_PEXPECT_SPIDER(scrapy.Spider):
    name = 'python_pexpect_spider'

    start_urls = ['https://pexpect.readthedocs.org/en/stable/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-pexpect'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
