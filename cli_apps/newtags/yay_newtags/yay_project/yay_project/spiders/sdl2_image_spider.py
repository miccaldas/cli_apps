import scrapy
#import snoop


class SDL2_IMAGE_SPIDER(scrapy.Spider):
    name = 'sdl2_image_spider'

    start_urls = ['https://github.com/libsdl-org/SDL_image']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'sdl2_image'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
