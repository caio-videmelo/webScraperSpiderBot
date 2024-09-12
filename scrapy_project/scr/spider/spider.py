from time import sleep
import scrapy
from scrapy.exporters import CsvItemExporter
from scrapy.exporters import CsvItemExporter

class GoodReadsSpider(scrapy.Spider):
    # Identidade
    name = 'quotebot'

    def __init__(self, *args, **kwargs):
        super(GoodReadsSpider, self).__init__(*args, **kwargs)
        # Open the CSV file in binary write mode
        self.file = open('quotes_data.csv', 'wb')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def close(self, reason):
        self.exporter.finish_exporting()
        self.file.close()

    # Request
    def start_requests(self):
        # Definir url(s) a varrer
        urls = ['https://www.goodreads.com/quotes?page=1']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Response
    def parse(self, response):
        # Process the returned response
        for elemento in response.xpath("//div[@class='quote']"):
            item = {
                'frase': elemento.xpath(".//div[@class='quoteText']/text()").get(),
                'autor': elemento.xpath(".//span[@class='authorOrTitle']/text()").get(),
                'tags': elemento.xpath(".//div[@class='greyText smallText left']/a/text()").getall(),
            }
            # Export the item using the exporter
            self.exporter.export_item(item)
            yield item  # Yield the item for Scrapy's pipeline

        # Find the link to the next page and extract the page number
        numero_proxima_pagina = response.xpath("//a[@class='next_page']/@href").get()
        if numero_proxima_pagina is not None:
            link_proxima_pagina = f'https://www.goodreads.com{numero_proxima_pagina}'
            yield scrapy.Request(url=link_proxima_pagina, callback=self.parse)
