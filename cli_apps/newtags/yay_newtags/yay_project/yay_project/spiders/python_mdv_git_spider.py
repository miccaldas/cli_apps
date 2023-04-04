import scrapy
#import snoop


class PYTHON_MDV_GIT_SPIDER(scrapy.Spider):
    name = 'python_mdv_git_spider'

    start_urls = ['https://github.com/axiros/terminal_markdown_viewer']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-mdv-git'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
