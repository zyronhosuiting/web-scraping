
# Web Scraping Project

This project is designed to scrape content from a specified website, extracting relevant information such as titles and article content for further use.

## Features

- Scrapes articles from a specified RSS feed.
- Extracts titles, content, and images from the articles.
- Supports saving the extracted data for use in other applications, such as posting to WordPress.

## Requirements

- Python 3.x
- Pipenv

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/zyronhosuiting/web-scraping.git
   cd web-scraping
   ```

2. **Install dependencies** using Pipenv:
   ```bash
   pipenv install
   ```

3. **Activate the virtual environment**:
   ```bash
   pipenv shell
   ```

## Usage

1. **Modify the script** to set the RSS feed URL you want to scrape.
2. **Run the scraper**:
   ```bash
   python3 ./rss/main.py or scrapy runspider ./cryptoCity/spiders/news_spider.py
   ```

## Example

The script will output the titles, content, and images for each article from the specified RSS feed.
