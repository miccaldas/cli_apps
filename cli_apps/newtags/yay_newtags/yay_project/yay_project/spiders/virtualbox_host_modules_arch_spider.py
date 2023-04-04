import scrapy
#import snoop


class VIRTUALBOX_HOST_MODULES_ARCH_SPIDER(scrapy.Spider):
    name = 'virtualbox_host_modules_arch_spider'

    start_urls = ['https://virtualbox.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'virtualbox-host-modules-arch'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
