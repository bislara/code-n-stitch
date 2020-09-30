from tkinter import *
from tkinter import ttk

import base64
import requests

from main import DETAILS


djeni98 = {'login': 'djeni98', 'id': 25268297, 'node_id': 'MDQ6VXNlcjI1MjY4Mjk3', 'avatar_url': 'https://avatars2.githubusercontent.com/u/25268297?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/djeni98', 'html_url': 'https://github.com/djeni98', 'followers_url': 'https://api.github.com/users/djeni98/followers', 'following_url': 'https://api.github.com/users/djeni98/following{/other_user}', 'gists_url': 'https://api.github.com/users/djeni98/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/djeni98/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/djeni98/subscriptions', 'organizations_url': 'https://api.github.com/users/djeni98/orgs', 'repos_url': 'https://api.github.com/users/djeni98/repos', 'events_url': 'https://api.github.com/users/djeni98/events{/privacy}', 'received_events_url': 'https://api.github.com/users/djeni98/received_events', 'type': 'User', 'site_admin': False, 'name': 'Djenifer', 'company': 'Ministério Público do Paraná (MPPR)', 'blog': '', 'location': 'Curitiba, Brazil', 'email': None, 'hireable': None, 'bio': 'Computer Science student and Web Developer Intern', 'twitter_username': None, 'public_repos': 11, 'public_gists': 0, 'followers': 3, 'following': 0, 'created_at': '2017-01-21T16:35:18Z', 'updated_at': '2020-09-29T22:20:16Z'}


def replace_space(string, idx):
    return string[:idx] + '\n' + string[idx+1:] if idx > -1 else string

root = Tk()
root.title('Github User Details')


# --- Configure Header --- #
header = Frame(root, bg='white')
header.pack_configure(fill='x')

github_img = PhotoImage(name='github', file='github.png')
Label(
    header,
    image=github_img,
    bg='white'
).grid_configure(row=0, column=0, padx=10, pady=10)

Label(
    header,
    text='Github User Details',
    font=('Helvetica', 12, 'bold'),
    bg='white',
).grid_configure(row=0, column=1, sticky=W)
# --- #


# --- Configure Searchbar --- #
searchbar = Frame(root)
searchbar.pack_configure(anchor='ne', pady=10, padx=5)

Label(
    searchbar,
    text='username',
    font='TkFixedFont'
).grid_configure(row=0, column=0)

style = ttk.Style()
style.configure('TEntry', padding=4)

user = StringVar()
user_input = ttk.Entry(searchbar, textvariable=user)
user_input.grid_configure(row=0, column=1, padx=5)

search_img = PhotoImage(name='search', file='search.png')
ttk.Button(
    searchbar,
    image=search_img,
    text='Search',
).grid_configure(row=0, column=2)
# --- #


# --- Configure Body --- #
body = Frame(root)
body.pack_configure(fill='x', pady=10, padx=5)

info_rows = DETAILS[1:]
user_data = djeni98

#  Image  #
response = requests.get(user_data['avatar_url'])
uri = base64.b64encode(response.content).decode('utf-8')

user_img = PhotoImage(name='user image', data=uri).subsample(2,2)
Label(
    body,
    image=user_img,
).grid_configure(row=0, column=0, rowspan=len(info_rows), padx=10, pady=10)

#  Info  #
for idx, (key, label) in enumerate(info_rows):
    Label(body, text=label).grid_configure(row=idx, column=1, sticky=W)
    if user_data[key] is None:
        Label(body, text='(not provided)').grid_configure(row=idx, column=2, sticky=W)
    else:
        if key == 'bio':
            text = user_data[key]
            text = replace_space(
                replace_space(text, text.find(' ', 53)), text.find(' ', 106)
            )
            ttk.Label(body, text=text).grid_configure(row=idx, column=2, sticky=W)
        else:
            ttk.Label(body, text=user_data[key]).grid_configure(row=idx, column=2, sticky=W)
# --- #

# --- Configure Footer --- #
footer = Frame(root)
footer.pack_configure(anchor='se', expand=True, pady=5, padx=5)

ttk.Button(
    footer,
    text='Close',
    command=lambda: root.destroy()
).grid_configure(row=0, column=0)


root.minsize(500, 200)
root.mainloop()
