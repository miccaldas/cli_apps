import scrapy
#import snoop


class QEMU_HW_S390X_VIRTIO_GPU_CCW_SPIDER(scrapy.Spider):
    name = 'qemu_hw_s390x_virtio_gpu_ccw_spider'

    start_urls = ['https://www.qemu.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'qemu-hw-s390x-virtio-gpu-ccw'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
