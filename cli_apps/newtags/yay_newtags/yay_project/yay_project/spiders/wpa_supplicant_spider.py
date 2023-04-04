import scrapy
#import snoop


class WPA_SUPPLICANT_SPIDER(scrapy.Spider):
    name = 'wpa_supplicant_spider'

    start_urls = ['https://w1.fi/wpa_supplicant/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'wpa_supplicant'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
