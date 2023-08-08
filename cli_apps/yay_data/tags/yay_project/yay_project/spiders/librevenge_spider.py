import scrapy
#import snoop


class LIBREVENGE_SPIDER(scrapy.Spider):
    name = 'librevenge_spider'

    start_urls = ['https://sf.net/p/libwpd/librevenge/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'librevenge'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
