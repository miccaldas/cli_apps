import scrapy
#import snoop


class QT5_X11EXTRAS_SPIDER(scrapy.Spider):
    name = 'qt5_x11extras_spider'

    start_urls = ['https://www.qt.io']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'qt5-x11extras'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
