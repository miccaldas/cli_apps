import scrapy

# import snoop


class SLUGIFY_SPIDER(scrapy.Spider):
    name = "slugify_spider"

    start_urls = ["https://pypi.org/project/python-slugify/"]

    # @snoop
    def parse(self, response):
        srch_text = response.xpath('///*[@id="description"]/div/p[1]/strong/text()').get()

        name = "slugify"

        lsts = srch_text
        results = {"name": name, "content": lsts}
        yield results
