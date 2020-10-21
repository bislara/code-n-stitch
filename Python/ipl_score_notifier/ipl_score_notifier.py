from bs4 import BeautifulSoup
import urllib.request
score_page = "http://static.cricinfo.com/rss/livescores.xml"
while True:
 page = urllib.request.urlopen(score_page)
 soup = BeautifulSoup(page, "html.parser")
 result = soup.find_all("description") 
 message = input("Do you want to refresh scores? [Y/N]")
 if message == "Y":
     print('------------------------------------------')
     for match in result:
         print(match.get_text())
 elif message == "N":
     break
 else:
     print('Please enter "Y" or "N" only.')
     continue