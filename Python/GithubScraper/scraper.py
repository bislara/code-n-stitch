import sys
import os
import requests
from bs4 import BeautifulSoup as Soup

username = sys.argv[1]
user_data = requests.get("https://github.com/{}".format(username))

print('''
----------------------------------
|     GITHUB PROFILE VIEWER      |
----------------------------------
''')

if os.path.isdir('profiles'):
    pass
else:
    os.mkdir('profiles')

data = {
    "username": username
}

if user_data.status_code == 200:
    html_text = Soup(user_data.text,'html.parser')

    api_data = requests.get("https://api.github.com/users/{}".format(username)).json()

    data["github_url"] = api_data["html_url"]
    user_profile_pic = api_data["avatar_url"]
    data["profile_url"] = user_profile_pic

    status = html_text.find('div',class_="user-status-message-wrapper").text.strip()
    data["status"] = status
    
    data["bio"] = api_data["bio"]

    details = {
        "name": api_data["name"],
        "followers":api_data["followers"],
        "following":api_data["following"],
        "company":api_data["company"],
        "portfolio":api_data["blog"],
        "location":api_data["location"],
        "email":api_data["email"],
        "twitter": api_data["twitter_username"],
    }

    for i,j in data.items():
        if j == None or j == '':
            data[i] = "  -  "

    for i,j in details.items():
        if j == None or j == '':
            if i == "twitter":
                if j == None or j == '':
                    details[i] = "  -  "
                else:
                    details[i] = f"https://www.twitter.com/{j}"
            details[i] = "  -  "

    info = f'''
-------------------
|    USER INFO    |
-------------------
Name         : {details["name"]}     
Username     : {data["username"]}    
profile pic  : {user_profile_pic}
profile URL  : {data["github_url"]}
website      : {details["portfolio"]}

-------------
|    BIO    |
-------------

[  {data["bio"]} ]

company        : {details["company"]}
current status : {data["status"]}
user location  : {details["location"]}
followers      : {details["followers"]}
following      : {details["following"]}

-----------------------
|  CONNECT WITH USER  |
-----------------------
Email     : {details["email"]}
Twitter   : {details["twitter"]}
company   : {details["company"]}
portfolio : {details["portfolio"]}

''' 
    print(info)
    status = input("Do you want to save this to a file? (Y/N) : ")
    if status.lower() == 'y':
        profile_dir = os.path.join(os.getcwd(),'profiles')
        user_file = os.path.join(profile_dir,f"{data['username']}.txt")
        
        with open(user_file,'w') as f:
            print("\nSaving file....\n")
            f.write(f'''                            ----------------------------------
                            |     GITHUB PROFILE VIEWER      |
                            ----------------------------------                     
{info}
''')
        print("File saved [100%]")
        print("\nThank you!!! \n\nplease follow, \nInstagram - https://www.instagram.com/sai_sumanth_951\nGithub - https://www.github.com/saisumanthkumar")

    else:
        print("\nThank you!!! \nplease follow \nInstagram - https://www.instagram.com/sai_sumanth_951\nGithub - https://www.github.com/saisumanthkumar")
        exit()
    
else:
    print("user doesn't exist")