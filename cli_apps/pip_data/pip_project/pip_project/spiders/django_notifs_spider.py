import scrapy
#import snoop


class DJANGO_NOTIFS_SPIDER(scrapy.Spider):
    name = 'django_notifs_spider'

    start_urls = ['https://github.com/danidee10/django-notifs']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'django-notifs'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
