import scrapy
#import snoop


class PKGCONF_SPIDER(scrapy.Spider):
    name = 'pkgconf_spider'

    start_urls = ['https://gitea.treehouse.systems/ariadne/pkgconf']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'pkgconf'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
