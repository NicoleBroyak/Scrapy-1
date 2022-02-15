import scrapy

class CategoriesSpider(scrapy.Spider):
    name = "categories"
    
    start_urls = [
        'https://books.toscrape.com'
    ]

    def parse(self, response):
        for category in response.xpath('.//ul[@class="nav nav-list"]/li/ul/li'):
            yield {'url': 'https://books.toscrape.com/' + category.xpath('.//a/@href').get(),}

#below result of using spider, I didn't know how to create books start urls
#using this spider, so to not waste time I used the json results from it
#I will appreciate feedback on how I could do that :)
categories_urls = [
"https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
"https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
"https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html",
"https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html",
"https://books.toscrape.com/catalogue/category/books/classics_6/index.html",
"https://books.toscrape.com/catalogue/category/books/philosophy_7/index.html",
"https://books.toscrape.com/catalogue/category/books/romance_8/index.html",
"https://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html",
"https://books.toscrape.com/catalogue/category/books/fiction_10/index.html",
"https://books.toscrape.com/catalogue/category/books/childrens_11/index.html",
"https://books.toscrape.com/catalogue/category/books/religion_12/index.html",
"https://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html",
"https://books.toscrape.com/catalogue/category/books/music_14/index.html",
"https://books.toscrape.com/catalogue/category/books/default_15/index.html",
"https://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html",
"https://books.toscrape.com/catalogue/category/books/sports-and-games_17/index.html",
"https://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html",
"https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html",
"https://books.toscrape.com/catalogue/category/books/new-adult_20/index.html",
"https://books.toscrape.com/catalogue/category/books/young-adult_21/index.html",
"https://books.toscrape.com/catalogue/category/books/science_22/index.html",
"https://books.toscrape.com/catalogue/category/books/poetry_23/index.html",
"https://books.toscrape.com/catalogue/category/books/paranormal_24/index.html",
"https://books.toscrape.com/catalogue/category/books/art_25/index.html",
"https://books.toscrape.com/catalogue/category/books/psychology_26/index.html",
"https://books.toscrape.com/catalogue/category/books/autobiography_27/index.html",
"https://books.toscrape.com/catalogue/category/books/parenting_28/index.html",
"https://books.toscrape.com/catalogue/category/books/adult-fiction_29/index.html",
"https://books.toscrape.com/catalogue/category/books/humor_30/index.html",
"https://books.toscrape.com/catalogue/category/books/horror_31/index.html",
"https://books.toscrape.com/catalogue/category/books/history_32/index.html",
"https://books.toscrape.com/catalogue/category/books/food-and-drink_33/index.html",
"https://books.toscrape.com/catalogue/category/books/christian-fiction_34/index.html",
"https://books.toscrape.com/catalogue/category/books/business_35/index.html",
"https://books.toscrape.com/catalogue/category/books/biography_36/index.html",
"https://books.toscrape.com/catalogue/category/books/thriller_37/index.html",
"https://books.toscrape.com/catalogue/category/books/contemporary_38/index.html",
"https://books.toscrape.com/catalogue/category/books/spirituality_39/index.html",
"https://books.toscrape.com/catalogue/category/books/academic_40/index.html",
"https://books.toscrape.com/catalogue/category/books/self-help_41/index.html",
"https://books.toscrape.com/catalogue/category/books/historical_42/index.html",
"https://books.toscrape.com/catalogue/category/books/christian_43/index.html",
"https://books.toscrape.com/catalogue/category/books/suspense_44/index.html",
"https://books.toscrape.com/catalogue/category/books/short-stories_45/index.html",
"https://books.toscrape.com/catalogue/category/books/novels_46/index.html",
"https://books.toscrape.com/catalogue/category/books/health_47/index.html",
"https://books.toscrape.com/catalogue/category/books/politics_48/index.html",
"https://books.toscrape.com/catalogue/category/books/cultural_49/index.html",
"https://books.toscrape.com/catalogue/category/books/erotica_50/index.html",
"https://books.toscrape.com/catalogue/category/books/crime_51/index.html"
]