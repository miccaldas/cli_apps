import scrapy
#import snoop


class QEMU_UI_SPICE_APP_SPIDER(scrapy.Spider):
    name = 'qemu_ui_spice_app_spider'

    start_urls = ['https://www.qemu.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'qemu-ui-spice-app'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
