import requests
import pandas as pd

API_KEY = '7a21a39b93e2a7c12212d30fff5f686a'  # Replace with your TMDb API key
url = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=en-US&page=1'

def fetch_tmdb_popular():
    response = requests.get(url)
    data = response.json()
    movies = []
    for movie in data.get('results', []):
        title = movie.get('title')
        year = movie.get('release_date', '')[:4]
        rating = movie.get('vote_average')
        movies.append({'title': title, 'year': year, 'rating': rating})
    return pd.DataFrame(movies)

if __name__ == "__main__":
    df = fetch_tmdb_popular()
    df.to_csv('tmdb_popular_movies.csv', index=False)
    print(f"Saved {len(df)} movies to CSV!")