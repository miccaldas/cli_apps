import scrapy
#import snoop


class MRTOOLSTHEME_SPIDER(scrapy.Spider):
    name = 'mrtoolstheme_spider'

    start_urls = ['https://gitlab.com/anatas_ch/pyl_mrtoolstheme']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'mrtoolstheme'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
