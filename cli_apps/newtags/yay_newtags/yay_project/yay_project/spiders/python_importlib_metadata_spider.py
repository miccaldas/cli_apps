import scrapy
#import snoop


class PYTHON_IMPORTLIB_METADATA_SPIDER(scrapy.Spider):
    name = 'python_importlib_metadata_spider'

    start_urls = ['https://importlib-metadata.readthedocs.io']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-importlib-metadata'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results