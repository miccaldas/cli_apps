import scrapy
#import snoop


class QCA_QT5_SPIDER(scrapy.Spider):
    name = 'qca_qt5_spider'

    start_urls = ['https://userbase.kde.org/QCA']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'qca-qt5'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results