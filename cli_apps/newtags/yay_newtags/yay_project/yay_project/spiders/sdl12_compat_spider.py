import scrapy
#import snoop


class SDL12_COMPAT_SPIDER(scrapy.Spider):
    name = 'sdl12_compat_spider'

    start_urls = ['https://github.com/libsdl-org/sdl12-compat']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'sdl12-compat'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
