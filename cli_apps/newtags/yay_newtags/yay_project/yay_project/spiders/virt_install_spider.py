import scrapy
#import snoop


class VIRT_INSTALL_SPIDER(scrapy.Spider):
    name = 'virt_install_spider'

    start_urls = ['https://virt-manager.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'virt-install'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
