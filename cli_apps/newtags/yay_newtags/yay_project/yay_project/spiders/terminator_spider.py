import scrapy
#import snoop


class TERMINATOR_SPIDER(scrapy.Spider):
    name = 'terminator_spider'

    start_urls = ['https://github.com/gnome-terminator/terminator']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'terminator'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
