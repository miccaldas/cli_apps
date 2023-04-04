import scrapy
#import snoop


class LIBCOLORD_SPIDER(scrapy.Spider):
    name = 'libcolord_spider'

    start_urls = ['https://www.freedesktop.org/software/colord']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libcolord'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
