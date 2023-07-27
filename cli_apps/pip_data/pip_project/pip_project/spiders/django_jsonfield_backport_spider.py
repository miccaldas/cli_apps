import scrapy
#import snoop


class DJANGO_JSONFIELD_BACKPORT_SPIDER(scrapy.Spider):
    name = 'django_jsonfield_backport_spider'

    start_urls = ['https://github.com/laymonage/django-jsonfield-backport']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'django-jsonfield-backport'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
