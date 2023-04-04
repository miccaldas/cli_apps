import scrapy
#import snoop


class EDK2_AARCH64_SPIDER(scrapy.Spider):
    name = 'edk2_aarch64_spider'

    start_urls = ['https://github.com/tianocore/tianocore.github.io/wiki/ArmVirtPkg']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'edk2-aarch64'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results