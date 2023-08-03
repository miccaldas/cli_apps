import scrapy
#import snoop


class PINENTRY_QT_SPIDER(scrapy.Spider):
    name = 'pinentry_qt_spider'

    start_urls = ['https://manpages.ubuntu.com/manpages/xenial/man1/pinentry-qt.1.html']

    #@snoop
    def parse(self, response):
        srch_gen = response.css('p::text').getall()
        srch_h1 = response.css('h1::text').getall()
        srch_h2 = response.css('h2::text').getall()
        srch_h3 = response.css('h3::text').getall()
        srch_h4 = response.css('h4::text').getall()
        srch_pre = response.css('pre::text').getall()
        srch_dd = response.css('dd::text').getall()
        name = 'pinentry-qt'

        hs = srch_h1 + srch_h2 + srch_h3 + srch_h4
        texts = srch_gen
        pres = srch_pre
        dds = srch_dd
        results = {'name': name, 'content': texts, 'titles': hs, 'ubuntus': pres, 'sourceforge': dds}
        yield results
