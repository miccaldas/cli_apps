import scrapy
#import snoop


class NOTES_MCLDS_SPIDER(scrapy.Spider):
    name = 'notes_mclds_spider'

    start_urls = ['https://github.com/miccaldas/notes']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'notes-mclds'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
