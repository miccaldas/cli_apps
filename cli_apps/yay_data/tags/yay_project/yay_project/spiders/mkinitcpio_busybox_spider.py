import scrapy
#import snoop


class MKINITCPIO_BUSYBOX_SPIDER(scrapy.Spider):
    name = 'mkinitcpio_busybox_spider'

    start_urls = ['https://www.busybox.net/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'mkinitcpio-busybox'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
