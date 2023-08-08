import scrapy
#import snoop


class XORG_BDFTOPCF_SPIDER(scrapy.Spider):
    name = 'xorg_bdftopcf_spider'

    start_urls = ['https://github.com/freedesktop/xorg-bdftopcf']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'xorg-bdftopcf'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
