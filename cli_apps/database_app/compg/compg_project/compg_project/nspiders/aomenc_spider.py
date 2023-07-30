import scrapy

# import snoop


class AOMENC_SPIDER(scrapy.Spider):
    name = "aomenc_spider"

    start_urls = ["https://github.com/master-of-zen/Av1an/blob/master/docs/Encoders/aomenc.md"]

    # @snoop
    def parse(self, response):
        srch_title = response.css("h1::text").getall()
        srch_enphasys = response.css("em::text").getall()
        srch_text = response.css("p::text").getall()

        name = "aomenc"
        lsts = srch_title + srch_enphasys + srch_text
        results = {"name": name, "content": lsts}
        yield results
