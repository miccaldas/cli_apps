import scrapy
#import snoop


class PYTHON_MARKDOWN_IT_PY_SPIDER(scrapy.Spider):
    name = 'python_markdown_it_py_spider'

    start_urls = ['https://github.com/executablebooks/markdown-it-py']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-markdown-it-py'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
