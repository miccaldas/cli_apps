import scrapy
#import snoop


class TTF_NERD_FONTS_SYMBOLS_2048_EM_MONO_SPIDER(scrapy.Spider):
    name = 'ttf_nerd_fonts_symbols_2048_em_mono_spider'

    start_urls = ['https://github.com/ryanoasis/nerd-fonts']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'ttf-nerd-fonts-symbols-2048-em-mono'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
