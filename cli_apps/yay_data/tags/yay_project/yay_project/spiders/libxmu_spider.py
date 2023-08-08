import scrapy
#import snoop


class LIBXMU_SPIDER(scrapy.Spider):
    name = 'libxmu_spider'

    start_urls = ['https://github.com/freedesktop/xorg-libxmu']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libxmu'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
