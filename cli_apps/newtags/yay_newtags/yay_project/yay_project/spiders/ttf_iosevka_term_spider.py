import scrapy
#import snoop


class TTF_IOSEVKA_TERM_SPIDER(scrapy.Spider):
    name = 'ttf_iosevka_term_spider'

    start_urls = ['https://typeof.net/Iosevka/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'ttf-iosevka-term'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
