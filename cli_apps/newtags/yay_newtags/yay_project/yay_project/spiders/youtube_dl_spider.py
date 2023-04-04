import scrapy
#import snoop


class YOUTUBE_DL_SPIDER(scrapy.Spider):
    name = 'youtube_dl_spider'

    start_urls = ['https://ytdl-org.github.io/youtube-dl/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'youtube-dl'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
