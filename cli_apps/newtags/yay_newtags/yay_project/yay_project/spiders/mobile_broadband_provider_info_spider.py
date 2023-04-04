import scrapy
#import snoop


class MOBILE_BROADBAND_PROVIDER_INFO_SPIDER(scrapy.Spider):
    name = 'mobile_broadband_provider_info_spider'

    start_urls = ['https://gitlab.gnome.org/GNOME/mobile-broadband-provider-info']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'mobile-broadband-provider-info'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
