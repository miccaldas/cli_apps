import scrapy
#import snoop


class NAUTILUS_GNOME_DISKS_SPIDER(scrapy.Spider):
    name = 'nautilus_gnome_disks_spider'

    start_urls = ['https://github.com/thebitstick/nautilus-gnome-disks']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'nautilus-gnome-disks'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
