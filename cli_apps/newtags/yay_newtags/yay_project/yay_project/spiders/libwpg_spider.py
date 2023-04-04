import scrapy
#import snoop


class LIBWPG_SPIDER(scrapy.Spider):
    name = 'libwpg_spider'

    start_urls = ['https://libwpg.sourceforge.net/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libwpg'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
