import scrapy
#import snoop


class BTRFS_PROGS_SPIDER(scrapy.Spider):
    name = 'btrfs_progs_spider'

    start_urls = ['https://btrfs.wiki.kernel.org']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'btrfs-progs'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
