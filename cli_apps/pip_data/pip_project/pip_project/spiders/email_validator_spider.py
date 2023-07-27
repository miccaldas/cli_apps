import scrapy
#import snoop


class EMAIL_VALIDATOR_SPIDER(scrapy.Spider):
    name = 'email_validator_spider'

    start_urls = ['https://github.com/JoshData/python-email-validator']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'email-validator'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
