import scrapy
#import snoop


class LIBSECRET_SPIDER(scrapy.Spider):
    name = 'libsecret_spider'

    start_urls = ['https://wiki.gnome.org/Projects/Libsecret']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libsecret'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
