import scrapy
#import snoop


class ET_XMLFILE_SPIDER(scrapy.Spider):
    name = 'et_xmlfile_spider'

    start_urls = ['https://foss.heptapod.net/openpyxl/et_xmlfile']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'et-xmlfile'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
