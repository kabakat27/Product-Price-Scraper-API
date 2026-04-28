# Product Price Scraper API

A simple Python API for scraping product prices from e-commerce websites.

## Features
- Scrape product prices from supported websites
- RESTful API interface
- Easy to extend for new sites

## Requirements
- Python 3.7+
- See `requirements.txt` for dependencies

## Installation
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd product-price-scraper-api
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Start the API server:
   ```bash
   python main.py
   ```
2. Use the API to scrape product prices. Example endpoint:
   ```http
   POST /scrape
   {
     "url": "https://example.com/product"
   }
   ```

## Project Structure
- `main.py` - Entry point and API server
- `scraper.py` - Scraping logic
- `models.py` - Data models
- `requirements.txt` - Python dependencies

## License
MIT License
