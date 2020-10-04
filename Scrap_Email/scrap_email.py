import requests
import re


def get_email(url):
    p = requests.get(url)
    emails_scrape = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", p.text, re.I))
    return emails_scrape

url = input("url to scrape : ")
print (get_email(url))