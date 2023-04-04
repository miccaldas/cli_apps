import scrapy
#import snoop


class REST_SPIDER(scrapy.Spider):
    name = 'rest_spider'

    start_urls = ['https://gitlab.gnome.org/GNOME/librest']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'rest'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
