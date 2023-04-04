import scrapy
#import snoop


class NTFS_3G_SPIDER(scrapy.Spider):
    name = 'ntfs_3g_spider'

    start_urls = ['https://www.tuxera.com/community/open-source-ntfs-3g/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'ntfs-3g'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
