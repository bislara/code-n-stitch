import os
import sys
import requests
from bs4 import BeautifulSoup

# function to get the html content of the page
def get_page():
    url = input('Enter a valid url: ')
    if url[:4] != 'http':
        print('Invalid url. Terminating program')
        sys.exit()
    res = requests.get(url)
    if not res.raise_for_status():
        return res
    else:
        print('Check internet connection, or try again. Terminating program')
        sys.exit()

# function to extract all links from the page
def get_links(res):
    soup = BeautifulSoup(res.text, 'html.parser')
    ls = [link.get('href') for link in soup.find_all('a') if (str(link.get('href')).startswith('http'))]
    title = soup.title.text
    return (ls, title)

# function to save file in the current directory
def save_file(ls, title):
    if not os.path.exists('./page_links'):
        os.mkdir('./page_links')
    fname = './page_links/' + '_'.join(title.split()) + '.txt'
    with open(fname, 'w', encoding='utf8') as outfile:
        content = '\n'.join(ls)
        outfile.write(content)
    print(f'File saved in directory {fname}')


if __name__ == '__main__':
    res = get_page()
    ls, title = get_links(res)
    save_file(ls, title)
