import scrapy
#import snoop


class DOCKER_SPIDER(scrapy.Spider):
    name = 'docker_spider'

    start_urls = ['https://www.docker.com/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'docker'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
