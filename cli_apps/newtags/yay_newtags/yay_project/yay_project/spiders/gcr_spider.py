import scrapy
#import snoop


class GCR_SPIDER(scrapy.Spider):
    name = 'gcr_spider'

    start_urls = ['https://gitlab.gnome.org/GNOME/gcr']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'gcr'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
