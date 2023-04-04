import scrapy
#import snoop


class ADOBE_SOURCE_CODE_PRO_FONTS_SPIDER(scrapy.Spider):
    name = 'adobe_source_code_pro_fonts_spider'

    start_urls = ['https://adobe-fonts.github.io/source-code-pro/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'adobe-source-code-pro-fonts'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
