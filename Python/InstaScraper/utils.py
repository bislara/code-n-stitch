import os
import requests

def create_file(data,profiles_dir):
    user_dir = os.path.join(profiles_dir,data["username"])
    if os.path.isdir(user_dir):
        print(f"\n{data['username']} profile already scraped\nUpdaing user profile.....\n")
    else:
        print("\ncreating user details folder...")
        os.mkdir(user_dir)
        print("Adding user deatils and user image\n")

    with open(os.path.join(user_dir,f"{data['username']}.txt"),"w",encoding="utf-8",errors='ignore') as text_file:
        text_file.write(
f'''------------
| username | - {data['username']}
------------
--------
| Name | - {data["name"]}
--------
-------------------
| profile_pic URL | - {data["image"]}
-------------------
-------
| Bio |
-------
{data["bio"]}

-------------
| followers | - {data["followers"]}
-------------
-------------
| following | - {data["following"]}
-------------''')
        print("\nsaving text file...")

    with open(os.path.join(user_dir,f"{data['username']}.png"),"wb") as image_file:
        image_file.write(requests.get(data["image"]).content)
        print("saving image file...")

    print("\nprocess completed - 100% [Added All required data]\n")