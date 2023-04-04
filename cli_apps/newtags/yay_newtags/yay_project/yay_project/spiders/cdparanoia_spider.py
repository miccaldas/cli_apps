import scrapy
#import snoop


class CDPARANOIA_SPIDER(scrapy.Spider):
    name = 'cdparanoia_spider'

    start_urls = ['https://www.xiph.org/paranoia/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'cdparanoia'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
