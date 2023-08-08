import scrapy
#import snoop


class LIBXVMC_SPIDER(scrapy.Spider):
    name = 'libxvmc_spider'

    start_urls = ['https://github.com/freedesktop/xorg-libxvmc']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libxvmc'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
