# IMDb Scraper

This project is a web scraping tool designed to extract movie data from IMDb's top movies chart. It fetches the titles, release years, and ratings of the top movies and stores the data in a CSV file.

## Project Structure

```
imdb-scraper
├── src
│   ├── scrape_imdb.py  # Main scraping logic
│   └── utils.py        # Utility functions (currently empty)
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/imdb-scraper.git
   cd imdb-scraper
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the scraper, execute the following command in your terminal:

```
python src/scrape_imdb.py
```

This will scrape the top movies from IMDb and save the data to a CSV file named `imdb_top_movies.csv`.

## Notes

- Ensure that scraping is allowed by checking the `robots.txt` file on IMDb.
- The `utils.py` file is currently empty but can be used for any additional utility functions needed for data processing or cleaning in the future.