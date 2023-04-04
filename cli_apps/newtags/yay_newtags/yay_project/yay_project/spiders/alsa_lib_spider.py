import scrapy
#import snoop


class ALSA_LIB_SPIDER(scrapy.Spider):
    name = 'alsa_lib_spider'

    start_urls = ['https://www.alsa-project.org']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'alsa-lib'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
