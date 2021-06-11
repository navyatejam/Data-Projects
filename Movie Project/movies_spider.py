import scrapy


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    start_urls = [
        'https://en.wikipedia.org/wiki/Lists_of_Telugu-language_films',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                quote
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)