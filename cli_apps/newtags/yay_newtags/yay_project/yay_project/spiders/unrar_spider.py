import scrapy
#import snoop


class UNRAR_SPIDER(scrapy.Spider):
    name = 'unrar_spider'

    start_urls = ['https://www.rarlab.com/rar_add.htm']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'unrar'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
