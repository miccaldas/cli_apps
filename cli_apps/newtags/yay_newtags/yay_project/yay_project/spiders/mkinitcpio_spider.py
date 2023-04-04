import scrapy
#import snoop


class MKINITCPIO_SPIDER(scrapy.Spider):
    name = 'mkinitcpio_spider'

    start_urls = ['https://gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'mkinitcpio'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results