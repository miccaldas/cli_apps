import scrapy
#import snoop


class WEBKIT2GTK_SPIDER(scrapy.Spider):
    name = 'webkit2gtk_spider'

    start_urls = ['https://webkitgtk.org']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'webkit2gtk'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
