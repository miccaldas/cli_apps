import scrapy
#import snoop


class PYTHON_BEAUTIFULSOUP4_SPIDER(scrapy.Spider):
    name = 'python_beautifulsoup4_spider'

    start_urls = ['https://www.crummy.com/software/BeautifulSoup/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-beautifulsoup4'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
