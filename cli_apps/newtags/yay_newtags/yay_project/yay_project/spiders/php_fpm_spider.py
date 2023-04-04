import scrapy
#import snoop


class PHP_FPM_SPIDER(scrapy.Spider):
    name = 'php_fpm_spider'

    start_urls = ['https://www.php.net/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'php-fpm'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
