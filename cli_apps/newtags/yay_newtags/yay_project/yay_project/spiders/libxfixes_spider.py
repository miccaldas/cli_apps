import scrapy
#import snoop


class LIBXFIXES_SPIDER(scrapy.Spider):
    name = 'libxfixes_spider'

    start_urls = ['https://github.com/freedesktop/xorg-libxfixes']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libxfixes'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
