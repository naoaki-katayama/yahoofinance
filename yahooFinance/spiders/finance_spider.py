import scrapy
from IPython import embed


class FinanceSpider(scrapy.Spider):
    name = "finance"

    def start_requests(self):
        urls = [
            'http://stocks.finance.yahoo.co.jp/stocks/detail/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print("ここからtest")
        # embed()
        self.log('Hi, this is an item page! %s' % response.url)
        # print(self)
        # print("ここからresponce.url")
        # print(response.url)
        # print("ここからresponce.body")
        # print(response.body)
        # print(response.body)
        # print(response.css('a').extract())

        # inner_text抽出
        # page_body = response.css('a::text').extract()

        # href抽出
        page_body = response.css('a::attr(href)').extract()
        # print(len(page_body))
        print("ここからaを順番に出力")
        for a in page_body:
            print(a)
        page = response.url.split("/")[-3]
        filename = 'finance-%s.html' % page
        print("filenameは{0}".format(filename))
        print(page_body)
        with open(filename, 'wb') as f:
            f.write(response.body)
            # f.write(page_body)
            # f.write("てすと")
            # f.close
        self.log('Saved file %s' % filename)
# command
# scrapy crawl finance
