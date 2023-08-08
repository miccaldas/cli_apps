import scrapy
#import snoop


class LIBFONTENC_SPIDER(scrapy.Spider):
    name = 'libfontenc_spider'

    start_urls = ['https://github.com/freedesktop/xorg-libfontenc']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libfontenc'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
