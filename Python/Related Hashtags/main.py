from bs4 import BeautifulSoup
import requests
import argparse


def get_related_hashtags(query, max_len=100):
    hashtags = []
    # We will scrape from this site 
    basic_url = 'http://best-hashtags.com/hashtag/'

    # Fetching
    print('Fetching Hashtags...')
    try:
        resp = requests.get(basic_url + query)
    except Exception as e:
        print('Somthing Went Wrong \n', e)

    soup = BeautifulSoup(resp.text, 'html.parser')

    all_hashtags_div = soup.find_all('div', {"class": "tag-box tag-box-v3 margin-bottom-40"})

    # If no hashtags are found 
    if not all_hashtags_div:
        print('No hashtags found. Search for more relevant topic')
        return []


    for div in all_hashtags_div:
        if div.text:
            hashtags += div.text.strip().split()
        if len(hashtags) >= max_len:
            break

    return list(set(hashtags))[:max_len]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Get related hastags from a given topic')
    parser.add_argument('-t', '--topic', required=True, help="Topic")
    parser.add_argument('-m', '--max-hashtags', required=False, help="Maximum number of hastags", type=int, default=100)

    arguments = parser.parse_args()

    print('Starting...')
    hashtags = get_related_hashtags(arguments.topic, arguments.max_hashtags)
    for hashtag in hashtags:
        print(hashtag)
    

    
