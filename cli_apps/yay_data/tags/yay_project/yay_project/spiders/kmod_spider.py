import scrapy
#import snoop


class KMOD_SPIDER(scrapy.Spider):
    name = 'kmod_spider'

    start_urls = ['https://git.kernel.org/pub/scm/utils/kernel/kmod/kmod.git']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'kmod'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
