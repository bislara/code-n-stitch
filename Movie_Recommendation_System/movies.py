import lxml
from bs4 import BeautifulSoup
from requests import get

class Movies:

    def __init__(self, genre_url):
        self.genre_url = "".join(["https://www.imdb.com", genre_url])
        self.soup = BeautifulSoup(get(self.genre_url).content, "lxml")
        self._list = []

    @property
    def list(self):
        if self._list:
            return self._list

        headings = self.soup.find_all("h3", class_="lister-item-header")
        self._list = [heading.text.replace("\n", " ") for heading in headings]
        return self._list
    
    def show_movies(self):
        for movie in self.list:
            print(movie)
