import scrapy
#import snoop


class RIPGREP_ALL_SPIDER(scrapy.Spider):
    name = 'ripgrep_all_spider'

    start_urls = ['https://github.com/phiresky/ripgrep-all']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'ripgrep-all'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
