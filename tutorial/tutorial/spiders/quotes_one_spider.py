import scrapy


class QuotesOneSpider(scrapy.Spider):
    name = "quotes_one"

    def start_requests(self):
        """
        Must return an iterable of Requests (list or write a generator function) which the Spider will begin to crawl.
        Subsequent requests will be generated successively from these initial requests.
        """
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        A method that will be called to handle the response downloaded for each of the requests made.
        The response parameter is an instance of TextResponse that holds the page content and has further helpful
        methods to handle it.
        The parse() usually parses the response, extracting the scraped data as dicts and also finding new URLs to
        follow and creating new requests (Request) from them
        """
        page = response.url.split('/')[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
