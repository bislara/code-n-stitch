from tkinter import *
from tkinter import ttk

from PIL import ImageTk

from main import DETAILS
from functions import get_user_details, insert_new_line, get_user_image

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
    command=lambda: search(user)
).grid_configure(row=0, column=2)
# --- #

def search(username):
    body.pack_forget()
    error.pack_forget()

    user = get_user_details(username.get())
    print(f'Searching {username.get()}')
    if user:
        body.pack_configure(fill='x', pady=10, padx=5)

        img = get_user_image(user['avatar_url']).resize((230, 230))
        user_img = ImageTk.PhotoImage(img)

        user_img_label.configure(image=user_img)
        user_img_label.image = user_img

        for idx, (key, label) in enumerate(info_rows):
            text = user[key] if user[key] is not None else '(not provided)'
            if key != 'bio':
                info_str_var[key].set(text)
            else:
                info_str_var[key].set(insert_new_line(text))
    else:
        error.pack_configure(pady=20)

# --- Configure Body --- #
container = Frame(root)
container.pack_configure(fill='x', pady=10, padx=5)

body = Frame(container)
# body.pack_configure(fill='x', pady=10, padx=5)

info_rows = DETAILS[1:]

user_img_label = Label(body, text='')
user_img_label.grid_configure(
    row=0, column=0, rowspan=len(info_rows), padx=10, pady=10
)

#  Info  #
info_str_var = {}
for idx, (key, label) in enumerate(info_rows):
    Label(body, text=label).grid_configure(row=idx, column=1, sticky=W)
    str_var = StringVar()
    str_label = Label(body, textvariable=str_var).grid_configure(row=idx, column=2, sticky=W)

    info_str_var[key] = str_var

#  Invalid User  #

error = Frame(container)
Label(error, text='Invalid User', fg='red', font=('Helvetica', 14, 'bold')).grid()

# --- #

# --- Configure Footer --- #
footer = Frame(root)
footer.pack_configure(anchor='se', expand=True, pady=5, padx=5)

ttk.Button(
    footer,
    text='Close',
    command=lambda: root.destroy()
).grid_configure(row=0, column=0)


root.bind('<Return>', lambda e: search(user))
root.minsize(500, 200)
root.mainloop()
