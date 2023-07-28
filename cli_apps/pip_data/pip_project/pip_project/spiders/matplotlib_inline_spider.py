import scrapy
#import snoop


class MATPLOTLIB_INLINE_SPIDER(scrapy.Spider):
    name = 'matplotlib_inline_spider'

    start_urls = ['https://github.com/ipython/matplotlib-inline']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'matplotlib-inline'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results