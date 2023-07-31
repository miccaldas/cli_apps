import scrapy
#import snoop


class PAMSCALE_SPIDER(scrapy.Spider):
    name = 'pamscale_spider'

    start_urls = ['https://linux.die.net/man/1/pamscale']

    #@snoop
    def parse(self, response):
        srch_text = response.xpath('//html/body/div[1]/div[2]/p').getall()
        name = 'pamscale'

        ct = []
        for s in srch_text:
            ps = s.replace('<p>', '').replace('</p>', '')
            bs = ps.replace('<b>', '').replace('</b>', '')
            ct.append(bs)
        for n in ct:
            if (
               n.startswith('Copyright')
               or n.startswith('[<i>')
               or n.startswith('<a href')
            ):
               ct.remove(n)
        clean_text = [i.strip() for i in ct]

        lists = clean_text
        results = {'name': name, 'content': lists}
        yield results
