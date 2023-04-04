import scrapy
#import snoop


class VIRTUALBOX_GUEST_ISO_SPIDER(scrapy.Spider):
    name = 'virtualbox_guest_iso_spider'

    start_urls = ['https://www.virtualbox.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'virtualbox-guest-iso'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
