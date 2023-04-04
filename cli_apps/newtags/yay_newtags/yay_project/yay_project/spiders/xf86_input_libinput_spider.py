import scrapy
#import snoop


class XF86_INPUT_LIBINPUT_SPIDER(scrapy.Spider):
    name = 'xf86_input_libinput_spider'

    start_urls = ['http://xorg.freedesktop.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'xf86-input-libinput'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
