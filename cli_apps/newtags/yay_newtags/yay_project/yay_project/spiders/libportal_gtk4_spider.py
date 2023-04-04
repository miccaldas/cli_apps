import scrapy
#import snoop


class LIBPORTAL_GTK4_SPIDER(scrapy.Spider):
    name = 'libportal_gtk4_spider'

    start_urls = ['https://github.com/flatpak/libportal']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libportal-gtk4'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
