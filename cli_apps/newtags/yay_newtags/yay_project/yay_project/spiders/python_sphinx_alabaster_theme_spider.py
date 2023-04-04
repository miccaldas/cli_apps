import scrapy
#import snoop


class PYTHON_SPHINX_ALABASTER_THEME_SPIDER(scrapy.Spider):
    name = 'python_sphinx_alabaster_theme_spider'

    start_urls = ['https://github.com/bitprophet/alabaster']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-sphinx-alabaster-theme'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
