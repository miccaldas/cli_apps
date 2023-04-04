import scrapy
#import snoop


class GLU_SPIDER(scrapy.Spider):
    name = 'glu_spider'

    start_urls = ['https://gitlab.freedesktop.org/mesa/glu']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'glu'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
