import scrapy
#import snoop


class LIBXDG_BASEDIR_SPIDER(scrapy.Spider):
    name = 'libxdg_basedir_spider'

    start_urls = ['https://github.com/devnev/libxdg-basedir']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libxdg-basedir'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
