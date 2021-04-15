import requests
import collections

SearchResults = collections.namedtuple("SearchResults",
                                       "imdb_code, title, director, keywords, duration, genres, rating, year, imdb_score")


def find_movie(search_text):

    if not search_text or not search_text.strip():
        raise ValueError("Search text is required")

    url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search_text)

    resp = requests.get(url)
    resp.raise_for_status()

    movie_data = resp.json()
    movie_list = movie_data.get('hits')

    movies = [
        SearchResults(**md)
        for md in movie_list
    ]

    movies.sort(key=lambda m: -m.year)
    return movies
