import scrapy
from .categories_spider import categories_urls

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = categories_urls

    def parse(self, response):
        for book in response.xpath('.//article[contains(concat(" ",normalize-space(@class)," ")," product_pod ")]'):
            yield {
                'title': book.xpath('.//h3/a/@title').get(),
                'price': book.xpath('.//div/p/text()').get().replace('\u00a3', ''),
                'book image url': book.xpath('.//div/a/img/@src').get().replace(
                    '../../../..', 'https://books.toscrape.com' ),
                'book details url': book.xpath('.//h3/a/@href').get().replace(
                    '../../..', 'https://books.toscrape.com/catalogue' ),
            }

        yield from response.follow_all(xpath='.//ul[@class="pager"]/li[@class="next"]/a/@href', callback=self.parse)