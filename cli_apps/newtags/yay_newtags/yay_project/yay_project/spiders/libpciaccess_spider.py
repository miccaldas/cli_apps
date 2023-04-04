import scrapy
#import snoop


class LIBPCIACCESS_SPIDER(scrapy.Spider):
    name = 'libpciaccess_spider'

    start_urls = ['https://github.com/freedesktop/xorg-libpciaccess']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libpciaccess'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
