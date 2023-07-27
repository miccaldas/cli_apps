import scrapy
#import snoop


class COLUMNIZE_SPIDER(scrapy.Spider):
    name = 'columnize_spider'

    start_urls = ['https://github.com/rocky/pycolumnize']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'columnize'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
