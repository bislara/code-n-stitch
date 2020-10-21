import requests
from pprint import pprint

# requests_cache, Can be extremely useful to cache the result and speedup
import requests_cache

requests_cache.install_cache()

'''
Wikipedia Api documentations 

Api used to search article
https://www.mediawiki.org/wiki/API:REST_API

Api used to generate article
https://en.wikipedia.org/api/rest_v1/#
 
If anyone know to do this suing only one api, please let me know
'''

search_query = input("Enter name of wikipedia article: ")
if search_query == "":
    search_query = 'Everest'

# Search the query in wikipedia for article name and title
search_results = requests.get('https://en.wikipedia.org/w/rest.php/v1/search/page',
                              params={'q': search_query, 'limit': 1}).json()
# pprint(search_results)  Do see the full response

best_search = search_results['pages'][0]  # We get all the info about everest wikipedia page

'''

After we we get the title for the required wikipedia article, then we generate summary for it

'key' contains the title name for as per url

In this example
This scraping get the summary for article    https://en.wikipedia.org/wiki/Mount_Everest

'''

page_result = requests.get('https://en.wikipedia.org/api/rest_v1/page/summary/' + best_search['key']).json()
# pprint(page_result)  #Do see the full response

# Actual Summary
summary = page_result['extract']

# Print it
print("Sumamry for Article ", search_query)
print(summary)
