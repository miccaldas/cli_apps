import scrapy
#import snoop


class QT5_WEBCHANNEL_SPIDER(scrapy.Spider):
    name = 'qt5_webchannel_spider'

    start_urls = ['https://www.qt.io']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'qt5-webchannel'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
