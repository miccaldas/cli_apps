import scrapy
#import snoop


class QEMU_UI_DBUS_SPIDER(scrapy.Spider):
    name = 'qemu_ui_dbus_spider'

    start_urls = ['https://www.qemu.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'qemu-ui-dbus'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results