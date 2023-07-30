import scrapy
#import snoop


class FSCK_VFAT_SPIDER(scrapy.Spider):
    name = 'fsck_vfat_spider'

    start_urls = ['https://linux.die.net/man/8/fsck.vfat']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'fsck.vfat'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
