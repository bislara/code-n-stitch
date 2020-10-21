from genres import Genres
from movies import Movies


def main():
    genre_url = Genres().select()
    movies = Movies(genre_url)
    movies.show_movies()


if __name__ == "__main__":
    main()