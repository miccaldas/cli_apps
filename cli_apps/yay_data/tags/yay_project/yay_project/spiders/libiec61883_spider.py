import scrapy
#import snoop


class LIBIEC61883_SPIDER(scrapy.Spider):
    name = 'libiec61883_spider'

    start_urls = ['https://www.kernel.org/pub/linux/libs/ieee1394/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libiec61883'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
