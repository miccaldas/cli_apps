import scrapy
#import snoop


class GSFONTS_SPIDER(scrapy.Spider):
    name = 'gsfonts_spider'

    start_urls = ['https://github.com/ArtifexSoftware/urw-base35-fonts']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'gsfonts'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
