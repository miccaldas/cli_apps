import scrapy
#import snoop


class VID_STAB_SPIDER(scrapy.Spider):
    name = 'vid_stab_spider'

    start_urls = ['http://public.hronopik.de/vid.stab']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'vid.stab'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
