import scrapy
#import snoop


class LIBVERTO_SPIDER(scrapy.Spider):
    name = 'libverto_spider'

    start_urls = ['https://github.com/latchset/libverto']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libverto'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
