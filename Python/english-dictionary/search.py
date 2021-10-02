"""Search through csv files for definitions."""
import csv
import json
import requests

class Search:
    """Perform search in csv file."""

    def __init__(self, csv_file):
        """
        Store csv object

        Args:
            csv_file (str): Path to dictionary csv file

        Return:
            None
  
        """

        self.d_file = csv_file

    def traverse(self, word):
        """
        Linear traversal of csv file.

        Args:
            word (str): Word to search for in csv

        Return:
            entries (list): List of csv entries that match the word

        """

        entries = []
        dict_f = self.d_file

        with open(dict_f, 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter='\n')
            for en in csv_reader:
                parts = en[0].replace('"', '') # Remove "
                parts = parts.split(',') # Split by ,
                entry_word = parts[0].lower() # Put entry word in lowercase
                search_word = word.lower() # Put search word in lowercase
                if entry_word == search_word:
                    entries.append(en) # Add entry that matches word
        
        return entries


class OnlineSearch(Search):
    """Perform definition in API call."""

    def __init__(self, csv_file, api_key):
        """
        Store csv object

        Args:
            csv_file (str): Path to dictionary csv file
            api_key (str): API key for rapidapi.com

        Return:
            None
  
        """
        Search.__init__(self, csv_file) # Instantiate super class
        self.api_key = api_key

    def online_search(self, word):
        """
        Do direct online search.

        Args:
            word (str): Word to search for in csv

        Return:
            definitions (list): List of online definitiions
  
        """

        url = f"https://rapidapi.p.rapidapi.com/words/{word}/definitions"

        headers = {
            'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
            'x-rapidapi-key': self.api_key
        }

        response = requests.request("GET", url, headers=headers)

        definitions = []

        if response.ok:
            result = json.loads(response.text)
            definitions = result['definitions']

        return definitions

    def search(self, word):
        """
        Searches csv file, if the word does not exist in the csv, search online.

        Args:
            word (str): Word to search for in csv

        Return:
            result (list):
  
        """

        result = self.traverse(word)
        if result == []:
            result = self.online_search(word)

        if result == []:
            raise Exception("Word could not be found in csv or retrieved online")

        return result
