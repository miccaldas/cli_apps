import scrapy

# import snoop


class ARCHLINUX_CONTRIB_SPIDER(scrapy.Spider):
    name = "archlinux_contrib_spider"

    start_urls = ["https://github.com/archlinux/contrib"]

    # @snoop
    def parse(self, response):
        srch_title = response.css("h1::text").getall()
        srch_enphasys = response.css("em::text").getall()
        srch_text = response.css("p::text").getall()

        name = "archlinux-contrib"
        lsts = srch_title + srch_enphasys + srch_text
        results = {"name": name, "content": lsts}
        yield results
