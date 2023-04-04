import scrapy
#import snoop


class XFSPROGS_SPIDER(scrapy.Spider):
    name = 'xfsprogs_spider'

    start_urls = ['https://xfs.wiki.kernel.org']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'xfsprogs'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
