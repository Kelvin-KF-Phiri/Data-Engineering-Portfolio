# TMDb Scraper

This project is a web scraping tool designed to extract movie data from tMDb's top movies chart. It fetches the titles, release years, and ratings of the top movies and stores the data in a CSV file.

## Usage

To run the scraper, execute the following command in your terminal:

```
python src/scrape_tmdb.py
```

This scraped the top movies from IMDb and save the data to a CSV file named `tmdb_top_movies.csv`.

## Notes

- Ensuree that scraping is allowed by checking the `robots.txt` file on TMDb.
- The `utils.py` file is currently empty but can be used for any additional utility functions needed for data processing or cleaning in the future.
