import scrapy
#import snoop


class LIBCDIO_PARANOIA_SPIDER(scrapy.Spider):
    name = 'libcdio_paranoia_spider'

    start_urls = ['https://www.gnu.org/software/libcdio/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libcdio-paranoia'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
