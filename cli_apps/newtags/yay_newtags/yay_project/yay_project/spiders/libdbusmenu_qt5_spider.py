import scrapy
#import snoop


class LIBDBUSMENU_QT5_SPIDER(scrapy.Spider):
    name = 'libdbusmenu_qt5_spider'

    start_urls = ['https://github.com/desktop-app/libdbusmenu-qt']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libdbusmenu-qt5'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
