import scrapy
#import snoop


class ZXING_CPP_SPIDER(scrapy.Spider):
    name = 'zxing_cpp_spider'

    start_urls = ['https://github.com/nu-book/zxing-cpp']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'zxing-cpp'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
