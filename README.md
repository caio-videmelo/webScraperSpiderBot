# Web Scraper Spider Bot

This project is a web scraper built with Scrapy, designed to extract quotes from Goodreads. The spider navigates through multiple pages of quotes and exports the data into a CSV file.

## Project Structure
scrapy_project/
└── scr/
└── spider/
├── spider.py
└── quotes_data.csv

- **spider.py**: The main Python script that contains the Scrapy spider for scraping quotes from Goodreads.

- **quotes_data.csv**: The output file where the scraped quotes, authors, and tags are stored.

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

Execute the spider using the following command:

```bash
scrapy runspider spider.py
```

3 - Output:

After the spider finishes running, you will find the quotes_data.csv file in the same directory, containing the scraped quotes, authors, and tags.

## Features

- Scrapes quotes from multiple pages on Goodreads.
- Exports the data into a CSV file for easy access and analysis.
- Handles pagination automatically.

## Contributing

Contributions are welcome! If you have suggestions for improvements or want to add features, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

Scrapy - The framework used for web scraping.

Goodreads - The website from which quotes are scraped.
