import scrapy
#import snoop


class LIBADWAITA_SPIDER(scrapy.Spider):
    name = 'libadwaita_spider'

    start_urls = ['https://gnome.pages.gitlab.gnome.org/libadwaita/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libadwaita'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
