import scrapy
#import snoop


class ABOUT_TIME_SPIDER(scrapy.Spider):
    name = 'about_time_spider'

    start_urls = ['https://github.com/rsalmei/about-time']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'about-time'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
