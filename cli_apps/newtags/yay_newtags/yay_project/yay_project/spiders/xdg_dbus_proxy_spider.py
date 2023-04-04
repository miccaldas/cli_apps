import scrapy
#import snoop


class XDG_DBUS_PROXY_SPIDER(scrapy.Spider):
    name = 'xdg_dbus_proxy_spider'

    start_urls = ['https://github.com/flatpak/xdg-dbus-proxy']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'xdg-dbus-proxy'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
