"""Search through csv files for definitions"""
import csv

class Search:
    """Perform search in csv file"""

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
        Linear traversal of csv file

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
