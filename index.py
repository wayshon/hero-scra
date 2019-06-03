import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = ['http://www.budejie.com/text/']

    # def start_requests(self):
    #     urls = [
    #         'http://quotes.toscrape.com/page/1/',
    #         'http://quotes.toscrape.com/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        lies = response.css('div.j-r-list >ul >li')
        for li in lies:
            username = li.css('a.u-user-name::text').extract()
            content = li.css('div.j-r-list-c-desc a::text').extract()
            yield {'username': username, 'content': content}