import scrapy
#import snoop


class LIBKSBA_SPIDER(scrapy.Spider):
    name = 'libksba_spider'

    start_urls = ['https://www.gnupg.org/related_software/libksba/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libksba'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
