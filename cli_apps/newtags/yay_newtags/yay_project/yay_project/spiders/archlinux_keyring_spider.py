import scrapy
#import snoop


class ARCHLINUX_KEYRING_SPIDER(scrapy.Spider):
    name = 'archlinux_keyring_spider'

    start_urls = ['https://gitlab.archlinux.org/archlinux/archlinux-keyring/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'archlinux-keyring'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
