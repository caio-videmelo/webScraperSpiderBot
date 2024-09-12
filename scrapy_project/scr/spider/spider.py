import scrapy
import csv
from time import sleep

class GoodReadsSpider(scrapy.Spider):
    """Spider to scrape quotes from Goodreads."""
    
    name = 'quotebot2'

    def start_requests(self):
        """Initialize requests to scrape the specified URLs."""
        urls = ['https://www.goodreads.com/quotes?page=1']
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """Parse the response and extract quote data."""
        for element in response.xpath("//div[@class='quote']"):
            yield {
                'quote': element.xpath(".//div[@class='quoteText']/text()").get(),
                'author': element.xpath(".//span[@class='authorOrTitle']/text()").get(),
                'tags': element.xpath(".//div[@class='greyText smallText left']/a/text()").getall(),
            }

        next_page_number = response.xpath("//a[@class='next_page']/@href").get()
        if next_page_number:
            next_page_url = f'https://www.goodreads.com/quotes?page={next_page_number.split("=")[1]}'
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def close(self, reason):
        """Export scraped data to a CSV file upon closing the spider."""
        with open('quotes.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['quote', 'author', 'tags']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for item in self.crawler.stats.get_value('item_scraped_count'):
                writer.writerow(item)
