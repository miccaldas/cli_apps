import scrapy
#import snoop


class ZSH_SPIDER(scrapy.Spider):
    name = 'zsh_spider'

    start_urls = ['https://www.zsh.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'zsh'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
