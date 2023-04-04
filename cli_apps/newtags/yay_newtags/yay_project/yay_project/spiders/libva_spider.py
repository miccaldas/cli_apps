import scrapy
#import snoop


class LIBVA_SPIDER(scrapy.Spider):
    name = 'libva_spider'

    start_urls = ['https://01.org/linuxmedia/vaapi']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libva'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
