import scrapy
#import snoop


class V4L_UTILS_SPIDER(scrapy.Spider):
    name = 'v4l_utils_spider'

    start_urls = ['https://linuxtv.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'v4l-utils'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
