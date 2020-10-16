import lxml
from bs4 import BeautifulSoup
from requests import get
import inquirer
from subprocess import call
import os


class Genres:
    LIST_URL = "https://www.imdb.com/feature/genre/?ref_=nv_ch_gr"

    def __init__(self):
        self.soup = BeautifulSoup(get(self.LIST_URL).content, "lxml")
        self._genres = {}

    @property
    def genres(self):
        if self._genres:
            return self._genres
        div = self.soup.find("div", class_="full-table")
        links = div.find_all(href=True)
        self._genres = {link.text.strip(): link["href"] for link in links}
        return self._genres

    def select(self):
        question = [inquirer.List(
            "genre",
            message="Which genre you want to watch",
            choices=list(self.genres.keys())),
        ]
        choise = inquirer.prompt(question)
        call("clear" if os.name =="posix" else "cls")
        return self.genres[choise["genre"]]
