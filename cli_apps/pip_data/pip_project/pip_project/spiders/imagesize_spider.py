import scrapy
#import snoop


class IMAGESIZE_SPIDER(scrapy.Spider):
    name = 'imagesize_spider'

    start_urls = ['https://github.com/shibukawa/imagesize_py']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'imagesize'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
