import scrapy
#import snoop


class VBOXIMG_MOUNT_SPIDER(scrapy.Spider):
    name = 'vboximg_mount_spider'

    start_urls = ['https://docs.oracle.com/en/virtualization/virtualbox/6.0/user/vboximg-mount.html']

    #@snoop
    def parse(self, response):
        srch_gen = response.css('p::text').getall()
        srch_h1 = response.css('h1::text').getall()
        srch_h2 = response.css('h2::text').getall()
        srch_h3 = response.css('h3::text').getall()
        srch_h4 = response.css('h4::text').getall()
        srch_pre = response.css('pre::text').getall()
        srch_dd = response.css('dd::text').getall()
        name = 'vboximg-mount'

        hs = srch_h1 + srch_h2 + srch_h3 + srch_h4
        texts = srch_gen
        pres = srch_pre
        dds = srch_dd
        results = {'name': name, 'content': texts, 'titles': hs, 'ubuntus': pres, 'sourceforge': dds}
        yield results
