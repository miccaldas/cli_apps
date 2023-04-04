import scrapy
#import snoop


class XORG_MKFONTSCALE_SPIDER(scrapy.Spider):
    name = 'xorg_mkfontscale_spider'

    start_urls = ['https://github.com/freedesktop/xorg-mkfontscale']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'xorg-mkfontscale'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
