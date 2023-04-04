import scrapy
#import snoop


class QGPGME_SPIDER(scrapy.Spider):
    name = 'qgpgme_spider'

    start_urls = ['https://www.gnupg.org/related_software/gpgme/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'qgpgme'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
