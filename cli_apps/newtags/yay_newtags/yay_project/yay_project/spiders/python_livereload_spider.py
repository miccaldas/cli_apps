import scrapy
#import snoop


class PYTHON_LIVERELOAD_SPIDER(scrapy.Spider):
    name = 'python_livereload_spider'

    start_urls = ['https://github.com/lepture/python-livereload']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-livereload'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
