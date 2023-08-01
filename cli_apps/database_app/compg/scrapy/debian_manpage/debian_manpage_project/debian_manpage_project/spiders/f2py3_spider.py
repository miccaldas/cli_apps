import scrapy

# import snoop


class F2PY3_SPIDER(scrapy.Spider):
    name = "f2py3_spider"

    start_urls = ["https://manpages.debian.org/unstable/python3-numpy/f2py3.1"]

    # @snoop
    def parse(self, response):
        srch_text = response.xpath("//*[@id='content']/div[2]/div/div/section[3]/p/text()").getall()

        srch_description = response.xpath("//*[@id='content']/div[2]/div/div/section[1]/p/text()").getall()
        name = "f2py3"

        lsts = srch_text + srch_description
        results = {"name": name, "content": lsts}
        yield results
