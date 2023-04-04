import scrapy
#import snoop


class LINUX_FIRMWARE_WHENCE_SPIDER(scrapy.Spider):
    name = 'linux_firmware_whence_spider'

    start_urls = ['https://git.kernel.org/?p=linux/kernel/git/firmware/linux-firmware.git;a=summary']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'linux-firmware-whence'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
