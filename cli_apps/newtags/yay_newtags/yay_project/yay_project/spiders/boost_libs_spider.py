import scrapy
#import snoop


class BOOST_LIBS_SPIDER(scrapy.Spider):
    name = 'boost_libs_spider'

    start_urls = ['https://www.boost.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'boost-libs'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
