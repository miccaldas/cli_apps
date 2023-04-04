import scrapy
#import snoop


class PYTHON_HTML2TEXT_SPIDER(scrapy.Spider):
    name = 'python_html2text_spider'

    start_urls = ['https://pypi.python.org/pypi/html2text/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-html2text'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
