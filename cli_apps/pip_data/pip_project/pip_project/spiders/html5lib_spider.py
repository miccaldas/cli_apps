import scrapy
#import snoop


class HTML5LIB_SPIDER(scrapy.Spider):
    name = 'html5lib_spider'

    start_urls = ['https://github.com/html5lib/html5lib-python']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'html5lib'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
