import scrapy
#import snoop


class LIBEVDEV_TWEAK_DEVICE_SPIDER(scrapy.Spider):
    name = 'libevdev_tweak_device_spider'

    start_urls = ['https://manpages.debian.org/testing/libevdev-tools/libevdev-tweak-device.1.en.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libevdev-tweak-device'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
