import scrapy
from scrapy.exporters import CsvItemExporter, XmlItemExporter, JsonItemExporter
from scrapy.loader import ItemLoader


class GoodReadsSpider(scrapy.Spider):
    """Spider to scrape quotes from Goodreads."""
    
    name = 'quotebot'

    def __init__(self, *args, **kwargs):
        """Initialize the spider and set up the exporters."""
        super(GoodReadsSpider, self).__init__(*args, **kwargs)
        # Open files for exporting data
        self.csv_file = open('quotes_data.csv', 'wb')
        self.xml_file = open('quotes_data.xml', 'wb')
        self.json_file = open('quotes_data.json', 'wb')

        # Set up exporters
        self.csv_exporter = CsvItemExporter(self.csv_file)
        self.xml_exporter = XmlItemExporter(self.xml_file)
        self.json_exporter = JsonItemExporter(self.json_file)

        # Start exporting
        self.csv_exporter.start_exporting()
        self.xml_exporter.start_exporting()
        self.json_exporter.start_exporting()

    def close(self, reason):
        """Finish exporting and close the files."""
        self.csv_exporter.finish_exporting()
        self.xml_exporter.finish_exporting()
        self.json_exporter.finish_exporting()
        self.csv_file.close()
        self.xml_file.close()
        self.json_file.close()

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

            # Export the item using the exporters
            self.csv_exporter.export_item(item)
            self.xml_exporter.export_item(item)
            self.json_exporter.export_item(item)

            yield item  # Yield the item for Scrapy's pipeline

        # Find the link to the next page and extract the page number
        next_page_number = response.xpath("//a[@class='next_page']/@href").get()
        if next_page_number is not None:
            next_page_link = f'https://www.goodreads.com{next_page_number}'
            yield scrapy.Request(url=next_page_link, callback=self.parse)
