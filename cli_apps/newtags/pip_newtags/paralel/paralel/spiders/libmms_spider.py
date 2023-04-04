import scrapy
#import snoop


class LIBMMS_SPIDER(scrapy.Spider):
    name = 'libmms_spider'

    start_urls = ['https://www.unix.com/man-page/opensolaris/3lib/libmms/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libmms'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
