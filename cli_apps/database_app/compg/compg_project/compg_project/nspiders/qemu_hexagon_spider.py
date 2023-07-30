import scrapy
#import snoop


class QEMU_HEXAGON_SPIDER(scrapy.Spider):
    name = 'qemu_hexagon_spider'

    start_urls = ['https://github.com/Comsecuris/qemu-hexagon']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'qemu-hexagon'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
