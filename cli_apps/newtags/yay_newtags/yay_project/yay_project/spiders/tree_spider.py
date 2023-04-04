import scrapy
#import snoop


class TREE_SPIDER(scrapy.Spider):
    name = 'tree_spider'

    start_urls = ['https://gitlab.com/OldManProgrammer/unix-tree']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'tree'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
