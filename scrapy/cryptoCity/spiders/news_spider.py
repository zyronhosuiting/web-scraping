import scrapy
from pathlib import Path


class NewsSpider(scrapy.Spider):
    name = "news_spider"

    def start_requests(self):
        start_urls = [
            "https://www.cryptocity.tw/news/grayscale-launches-aave-trust",  # Replace with the target URL
        ]

        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
