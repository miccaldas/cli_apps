import scrapy
#import snoop


class FZF_SPIDER(scrapy.Spider):
    name = 'fzf_spider'

    start_urls = ['https://github.com/junegunn/fzf']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'fzf'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
