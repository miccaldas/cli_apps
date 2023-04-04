import scrapy
#import snoop


class DOCX2TXT_SPIDER(scrapy.Spider):
    name = 'docx2txt_spider'

    start_urls = ['http://docx2txt.sourceforge.net']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'docx2txt'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
