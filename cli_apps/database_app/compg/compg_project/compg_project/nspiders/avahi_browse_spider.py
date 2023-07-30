import scrapy
#import snoop


class AVAHI_BROWSE_SPIDER(scrapy.Spider):
    name = 'avahi_browse_spider'

    start_urls = ['https://linux.die.net/man/1/avahi-browse']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'avahi-browse'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
