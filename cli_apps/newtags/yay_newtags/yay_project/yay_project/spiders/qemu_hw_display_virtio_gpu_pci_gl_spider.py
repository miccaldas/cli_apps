import scrapy
#import snoop


class QEMU_HW_DISPLAY_VIRTIO_GPU_PCI_GL_SPIDER(scrapy.Spider):
    name = 'qemu_hw_display_virtio_gpu_pci_gl_spider'

    start_urls = ['https://www.qemu.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'qemu-hw-display-virtio-gpu-pci-gl'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
