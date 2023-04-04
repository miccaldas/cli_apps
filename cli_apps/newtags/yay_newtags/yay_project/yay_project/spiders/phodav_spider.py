import scrapy
#import snoop


class PHODAV_SPIDER(scrapy.Spider):
    name = 'phodav_spider'

    start_urls = ['https://wiki.gnome.org/phodav']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'phodav'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
