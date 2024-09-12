# Web Scraper Spider Bot

This project contains a Scrapy spider designed to scrape quotes from the Goodreads website. The spider extracts quotes, authors, and tags, and exports the scraped data into multiple formats: CSV, XML, and JSON.

## Project Structure
scrapy_project/
└── scr/
└── spider/
├── spider.py
└── quotes_data.csv
└── quotes_data.xml
└── quotes_data.json

- **spider.py**: The main Python script that contains the Scrapy spider for scraping quotes from Goodreads.

- **quotes_data.csv**: The output file where the scraped quotes, authors, and tags are stored.

- **quotes_data.xml**: The output file where the scraped quotes, authors, and tags are stored.

- **quotes_data.json**: The output file where the scraped quotes, authors, and tags are stored.

## Requirements

To run this project, you need to have the following installed:

- Python 3.x

- Scrapy

You can install Scrapy using pip:

```bash
pip install scrapy
```

## Usage

1 - Clone the repository:

```bash
git clone https://github.com/caio-videmelo/webScraperSpiderBot.git
cd webScraperSpiderBot/scrapy_project/scr/spider
```
2 - Run the spider:

Execute the spider using the following command (replace the *nameOfBot* with the identification you use for the bot into the python code, I used quotebot, but you can change it):

```bash
scrapy crawl *nameOfBot*
```

3 - Output:

After the spider finishes running, you will find the quotes_data.csv, quotes_data.xml and the quotes_data.json files in the same directory, containing the scraped quotes, authors, and tags.

## Features

- Scrapes quotes from multiple pages on Goodreads.
- Exports the data into CSV, JSON and XML files for easy access and analysis.
- Handles pagination automatically.

## Code Explanation

### Spider Overview

The spider is defined in the GoodReadsSpider class, which inherits from scrapy.Spider. The main components of the spider are:

#### Initialization:

The constructor (__init__) opens files for exporting data in CSV, XML, and JSON formats and initializes the respective exporters.

#### Start Requests:

The start_requests method defines the initial URL to scrape, which is the first page of quotes on Goodreads.

#### Parsing Responses:

The parse method processes the response from the requests. It extracts the quote text, author, and tags using XPath selectors, loads the data into an item, and exports it to CSV, XML, and JSON formats.

#### Closing the Spider:

The close method is called when the spider finishes running. It finalizes the exporting process and closes all opened files.

#### Export Functions

The spider includes functions to export scraped data into different formats:

CSV Export:

The CsvItemExporter is used to write the scraped data into a CSV file named quotes_data.csv.

XML Export:

The XmlItemExporter is used to write the scraped data into an XML file named quotes_data.xml.

JSON Export:

The JsonItemExporter is used to write the scraped data into a JSON file named quotes_data.json.

## Contributing

Contributions are welcome! If you have suggestions for improvements or want to add features, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

Scrapy - The framework used for web scraping.

Goodreads - The website from which quotes are scraped.
