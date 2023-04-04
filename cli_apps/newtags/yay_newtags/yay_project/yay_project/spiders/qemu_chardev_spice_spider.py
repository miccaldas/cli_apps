import scrapy
#import snoop


class QEMU_CHARDEV_SPICE_SPIDER(scrapy.Spider):
    name = 'qemu_chardev_spice_spider'

    start_urls = ['https://www.qemu.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'qemu-chardev-spice'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
