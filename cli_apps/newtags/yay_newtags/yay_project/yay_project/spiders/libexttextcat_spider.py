import scrapy
#import snoop


class LIBEXTTEXTCAT_SPIDER(scrapy.Spider):
    name = 'libexttextcat_spider'

    start_urls = ['https://wiki.documentfoundation.org/Libexttextcat']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libexttextcat'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
