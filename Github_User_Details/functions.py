import requests

from io import BytesIO
from PIL import Image


def get_user_image(url):
    response = requests.get(url)
    img_file = BytesIO(response.content)
    return Image.open(img_file)


def get_user_details(username):
    res = requests.get(f'https://api.github.com/users/{username}')
    return res.json() if res.status_code == 200 else None


def replace_space(string, idx):
    return string[:idx] + '\n' + string[idx+1:] if idx > -1 else string


def insert_new_line(string):
    return replace_space(
        replace_space(string, string.find(' ', 53)), string.find(' ', 106)
    )
