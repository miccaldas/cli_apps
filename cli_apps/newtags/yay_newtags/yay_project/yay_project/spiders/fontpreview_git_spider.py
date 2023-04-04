import scrapy
#import snoop


class FONTPREVIEW_GIT_SPIDER(scrapy.Spider):
    name = 'fontpreview_git_spider'

    start_urls = ['https://github.com/sdushantha/fontpreview']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'fontpreview-git'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
