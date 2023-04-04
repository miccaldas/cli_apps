import scrapy
#import snoop


class XORG_SERVER_XVFB_SPIDER(scrapy.Spider):
    name = 'xorg_server_xvfb_spider'

    start_urls = ['https://xorg.freedesktop.org']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'xorg-server-xvfb'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
