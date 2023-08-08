import scrapy
#import snoop


class POLKIT_QT5_SPIDER(scrapy.Spider):
    name = 'polkit_qt5_spider'

    start_urls = ['https://www.kde.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'polkit-qt5'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
