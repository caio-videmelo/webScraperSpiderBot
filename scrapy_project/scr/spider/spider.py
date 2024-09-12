from time import sleep
import scrapy
from scrapy.exporters import CsvItemExporter

class GoodReadsSpider(scrapy.Spider):
    """Spider to scrape quotes from Goodreads."""
    
    name = 'quotebot'

    def __init__(self, *args, **kwargs):
        """Initialize the spider and set up the CSV exporter."""
        super(GoodReadsSpider, self).__init__(*args, **kwargs)
        # Open the CSV file in binary write mode
        self.file = open('quotes_data.csv', 'wb')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def close(self, reason):
        """Finish exporting and close the CSV file."""
        self.exporter.finish_exporting()
        self.file.close()

    def start_requests(self):
        """Initialize requests to scrape the specified URLs."""
        # Define the URL(s) to scrape
        urls = ['https://www.goodreads.com/quotes?page=1']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """Process the returned response and extract quote data."""
        for element in response.xpath("//div[@class='quote']"):
            item = {
                'quote': element.xpath(".//div[@class='quoteText']/text()").get(),
                'author': element.xpath(".//span[@class='authorOrTitle']/text()").get(),
                'tags': element.xpath(".//div[@class='greyText smallText left']/a/text()").getall(),
            }
            # Export the item using the exporter
            self.exporter.export_item(item)
            yield item  # Yield the item for Scrapy's pipeline

        # Find the link to the next page and extract the page number
        next_page_number = response.xpath("//a[@class='next_page']/@href").get()
        if next_page_number is not None:
            next_page_link = f'https://www.goodreads.com{next_page_number}'
            yield scrapy.Request(url=next_page_link, callback=self.parse)
