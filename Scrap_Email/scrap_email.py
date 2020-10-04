import requests
import re
from bs4 import BeautifulSoup
import urllib.request as urllib2

def get_url(url):
    urls = []
    conn = urllib2.urlopen(url)
    html = conn.read()

    soup = BeautifulSoup(html, features="lxml")
    links = soup.find_all('a')

    for tag in links:
        link = tag.get('href',None)
        if (link is not None and link != '' and link[0] == '/' and link not in urls) :
            urls.append(link)
    return urls

def get_email(url):
    emails = set()
    all_urls = get_url(url)
    print("1/" + str(len(all_urls) + 1) +" scraping email from " + url)
    p = requests.get(url)
    emails_scrape = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", p.text, re.I))
    emails |= emails_scrape
    i = 2
    for link in all_urls:
        print(str(i) + "/" + str(len(all_urls) + 1) +" scraping email from " + str(url + link))
        p = requests.get(str(url + link))
        emails_scrape = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", p.text, re.I))
        emails |= emails_scrape
        i += 1
    return emails

url = input("url to scrape : ")
print (get_email(url))


