import scrapy
#import snoop


class TOTEM_PL_PARSER_SPIDER(scrapy.Spider):
    name = 'totem_pl_parser_spider'

    start_urls = ['https://gitlab.gnome.org/GNOME/totem-pl-parser']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'totem-pl-parser'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
