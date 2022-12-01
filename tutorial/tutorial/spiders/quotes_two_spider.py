import scrapy


class QuotesTwoSpider(scrapy.Spider):
    name = "quotes_two"

    start_urls = [
        'https://quotes.toscrape.com',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').getall()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
