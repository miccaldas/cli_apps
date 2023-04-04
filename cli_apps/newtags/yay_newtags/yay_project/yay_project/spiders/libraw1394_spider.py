import scrapy
#import snoop


class LIBRAW1394_SPIDER(scrapy.Spider):
    name = 'libraw1394_spider'

    start_urls = ['https://ieee1394.wiki.kernel.org/index.php/Main_Page']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libraw1394'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
