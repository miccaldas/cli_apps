import scrapy
#import snoop


class MDV_SPIDER(scrapy.Spider):
    name = 'mdv_spider'

    start_urls = ['http://github.com/axiros/terminal_markdown_viewer']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'mdv'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results