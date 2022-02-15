import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    ]

    def parse(self, response):
        for quote in response.css('article.product_pod'):
            yield {
                'text': quote.css('h3').get(),
            }
