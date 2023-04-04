import scrapy
#import snoop


class LIBXSLT_SPIDER(scrapy.Spider):
    name = 'libxslt_spider'

    start_urls = ['https://gitlab.gnome.org/GNOME/libxslt/-/wikis/home']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libxslt'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
