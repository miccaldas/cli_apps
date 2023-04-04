import scrapy
#import snoop


class QEMU_HW_DISPLAY_VIRTIO_VGA_SPIDER(scrapy.Spider):
    name = 'qemu_hw_display_virtio_vga_spider'

    start_urls = ['https://www.qemu.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'qemu-hw-display-virtio-vga'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
