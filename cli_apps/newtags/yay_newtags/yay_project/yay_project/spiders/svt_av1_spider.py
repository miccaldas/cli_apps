import scrapy
#import snoop


class SVT_AV1_SPIDER(scrapy.Spider):
    name = 'svt_av1_spider'

    start_urls = ['https://gitlab.com/AOMediaCodec/SVT-AV1']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'svt-av1'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
