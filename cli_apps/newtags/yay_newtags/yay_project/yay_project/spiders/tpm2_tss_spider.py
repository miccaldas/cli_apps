import scrapy
#import snoop


class TPM2_TSS_SPIDER(scrapy.Spider):
    name = 'tpm2_tss_spider'

    start_urls = ['https://github.com/tpm2-software/tpm2-tss']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'tpm2-tss'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
