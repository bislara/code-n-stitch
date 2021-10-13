from selenium import webdriver
import time
from utils import create_file
import sys
import os

driver = webdriver.Chrome('chromedriver.exe')
time.sleep(5)
print('----------------------------------------------------------------\n'
      '|               WELCOME TO INSTAGRAM PROFILE SCRAPER           |\n'
      '----------------------------------------------------------------\n')
driver.get('https://www.instagram.com')
USERNAME = input('USERNAME : ')
PASSWORD = input('PASSWORD : ')
time.sleep(2)
while len(PASSWORD) < 8:
    print("Please enter valid password")
    PASSWORD = input('PASSWORD : ')

driver.find_element_by_css_selector('input[type="text"]').send_keys(USERNAME)
driver.find_element_by_css_selector('input[type="password"]').send_keys(PASSWORD)
driver.find_element_by_css_selector('button[type="submit"]').click()
time.sleep(3)

while driver.current_url == "https://www.instagram.com/":
    print("\nplease check your username and password\n")
    quit()

time.sleep(2)
print("\nSuccessfully logged in \n")
profiles_dir = os.path.join(os.getcwd(),"profiles")
if os.path.isdir("profiles"):
    print("Folder already exits,pleaselook into it for scrap profiles")
else:
    os.mkdir("profiles")
    print("creating profiles folder to store details")

all_buttons = driver.find_elements_by_css_selector('button[type="button"]')

for i in all_buttons:
    if i.text == "Not Now":
        i.click()
partial = driver.find_element_by_css_selector('div[role="dialog"]')
partial.find_elements_by_tag_name('button')[1].click()
9701049363

while True:
    print('''
Welcome to Instagram Profile scraper,
1. Scrape a profile
2. Quit
    ''')
    choice = input("choose a option : ")
    if choice == "1":
        print("You have opted to scrap a profile")
        while True:
            print('   =>  Note : If you want to go main menu type "0" ')
            username = input("Enter a username to scrape : ")
            if username != "0":
                data = {
                "username":username,
                }
                driver.get(f'https://www.instagram.com/{username}')
                image_link = driver.find_element_by_tag_name('img').get_attribute('src')
                data["image"] = image_link

                followers = driver.find_element_by_partial_link_text('followers').text
                following = driver.find_element_by_partial_link_text('following').text

                data["followers"] = followers
                data["following"] = following

                bio_data = driver.find_element_by_css_selector('.-vDIg')
                name = bio_data.find_element_by_tag_name('h1').text
                if name == '':
                    name = data["username"]
                data["name"] = name
                bio = bio_data.find_element_by_css_selector('div span').text
                if bio == '':
                    bio = "user hasn't added any bio"
                data["bio"] = bio
                create_file(data,profiles_dir)
            else:
                break

    elif choice == "2":
        print("Logging Out....\nThankyou!!! for using\nplease follow https://www.github.com/saisumanthkumar or https://www.instagram.com/sai_sumanth_951")
        driver.close()
        break
    else:
        print("Enter a valid Option")