import scrapy
#import snoop


class QEMU_SYSTEM_SPARC_FIRMWARE_SPIDER(scrapy.Spider):
    name = 'qemu_system_sparc_firmware_spider'

    start_urls = ['https://www.qemu.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'qemu-system-sparc-firmware'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
