import scrapy
#import snoop


class VIRT_LOGIN_SHELL_SPIDER(scrapy.Spider):
    name = 'virt_login_shell_spider'

    start_urls = ['https://helpmanual.io/help/virt-login-shell/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'virt-login-shell'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
