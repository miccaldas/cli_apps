import scrapy
#import snoop


class XORG_XGAMMA_SPIDER(scrapy.Spider):
    name = 'xorg_xgamma_spider'

    start_urls = ['https://github.com/freedesktop/xorg-xgamma']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'xorg-xgamma'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results