import requests 
from bs4 import BeautifulSoup


HEADERS = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

DOWNLOAD_URL = "https://yts-subs.com/"


def get_movie(query):
    url = DOWNLOAD_URL + 'search/' + query
    response = requests.get(url, HEADERS)
    print("response status code: ",response.status_code)
    soup = BeautifulSoup(response.content, features='html.parser')
    div_tags = soup.find_all('div',{'class':'media-body'})
    links = [i.findChildren('a', recursive=False)[0]['href'] for i in div_tags]
    names = soup.find_all('h3', {'class': 'media-heading'})
    names = [i.get_text() for i in names]
    # print(names)
    return links, names

def choose_movie(links, names):
    print('Select movie:')
    for i in range(len(names)):
        print(f"{i}. {names[i]}")
    sel = int(input())
    return DOWNLOAD_URL + links[sel]

def sel_sub(url):
    response = requests.get(url, HEADERS)
    # print(response.status_code)
    soup = BeautifulSoup(response.content, features='html.parser')
    dl_links = soup.find_all('a',{'class':'subtitle-download'})
    dl_links = [i['href'] for i in dl_links]
    print('Select sub:')
    for i in range(len(dl_links)):
        print(f"{i}. {dl_links[i]}")
    sel = int(input())
    return DOWNLOAD_URL + dl_links[sel]


def main_dl(url):
    response = requests.get(url, HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    link = soup.find_all('a',{'class': 'btn-icon download-subtitle'})
    link = link[0]['href']
    print(f"Ctrl + Click here:{link}")


if __name__ == "__main__":
    links, names = get_movie(input("Enter movie to download of:"))
    if not links:
        print("No movies found")
    else:
        url = choose_movie(links, names)
        url = sel_sub(url)
        main_dl(url)