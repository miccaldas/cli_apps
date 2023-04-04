import scrapy
#import snoop


class PERL_FILE_NEXT_SPIDER(scrapy.Spider):
    name = 'perl_file_next_spider'

    start_urls = ['https://metacpan.org/release/File-Next']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'perl-file-next'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
