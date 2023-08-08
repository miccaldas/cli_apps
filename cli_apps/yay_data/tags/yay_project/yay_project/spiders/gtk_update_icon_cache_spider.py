import scrapy
#import snoop


class GTK_UPDATE_ICON_CACHE_SPIDER(scrapy.Spider):
    name = 'gtk_update_icon_cache_spider'

    start_urls = ['https://www.gtk.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'gtk-update-icon-cache'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
