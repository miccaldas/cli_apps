import scrapy
#import snoop


class CHECK_BROKEN_PACKAGES_PACMAN_HOOK_GIT_SPIDER(scrapy.Spider):
    name = 'check_broken_packages_pacman_hook_git_spider'

    start_urls = ['https://github.com/desbma/pacman-hooks']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'check-broken-packages-pacman-hook-git'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
