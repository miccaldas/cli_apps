import scrapy
#import snoop


class CANTARELL_FONTS_SPIDER(scrapy.Spider):
    name = 'cantarell_fonts_spider'

    start_urls = ['https://gitlab.gnome.org/GNOME/cantarell-fonts']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'cantarell-fonts'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
