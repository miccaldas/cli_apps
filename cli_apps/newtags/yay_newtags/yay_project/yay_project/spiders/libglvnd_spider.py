import scrapy
#import snoop


class LIBGLVND_SPIDER(scrapy.Spider):
    name = 'libglvnd_spider'

    start_urls = ['https://gitlab.freedesktop.org/glvnd/libglvnd']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libglvnd'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results