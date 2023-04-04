import scrapy
#import snoop


class GNU_FREE_FONTS_SPIDER(scrapy.Spider):
    name = 'gnu_free_fonts_spider'

    start_urls = ['https://www.gnu.org/software/freefont/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'gnu-free-fonts'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
