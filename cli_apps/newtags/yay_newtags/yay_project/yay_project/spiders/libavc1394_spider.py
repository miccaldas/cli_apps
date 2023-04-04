import scrapy
#import snoop


class LIBAVC1394_SPIDER(scrapy.Spider):
    name = 'libavc1394_spider'

    start_urls = ['https://sourceforge.net/projects/libavc1394/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libavc1394'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
