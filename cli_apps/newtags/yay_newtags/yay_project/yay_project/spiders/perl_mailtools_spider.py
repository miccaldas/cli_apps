import scrapy
#import snoop


class PERL_MAILTOOLS_SPIDER(scrapy.Spider):
    name = 'perl_mailtools_spider'

    start_urls = ['https://metacpan.org/release/MailTools']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'perl-mailtools'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
