import scrapy
#import snoop


class UNZIP_SPIDER(scrapy.Spider):
    name = 'unzip_spider'

    start_urls = ['http://infozip.sourceforge.net/UnZip.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'unzip'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
