import tkinter as tk

from tkinter import ttk

from PIL import ImageTk

from main import DETAILS
from functions import get_user_details, insert_new_line, get_user_image

info_rows = DETAILS[1:]


class Header(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.img = tk.PhotoImage(file='github.png')

        self.label_img = tk.Label(self, image=self.img, bg='white')
        self.label_img.grid(row=0, column=0, padx=10, pady=10)

        font = ('Helvetica', 12, 'bold')
        self.title = tk.Label(
            self, text='Github User Details', bg='white', font=font
        )
        self.title.grid(row=0, column=1, sticky=tk.W)


class SearchBar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.label = tk.Label(self, text='username', font='TkFixedFont')
        self.label.grid(row=0, column=0)

        style = ttk.Style()
        style.configure('TEntry', padding=4)

        self.username = tk.StringVar()
        self.input = ttk.Entry(self, textvariable=self.username)
        self.input.grid(row=0, column=1, padx=5)
        self.input.focus()

        self.img = tk.PhotoImage(name='search', file='search.png')
        self.button = ttk.Button(
            self, image=self.img, text='Search', command=self.search
        )
        self.button.grid(row=0, column=2)

        self.bind_all('<Return>', lambda e: self.search())

    def search(self):
        return self.parent.search(self.username.get())


class UserContent(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.img_label = tk.Label(self, text='')
        self.img_label.grid(
            row=0, column=0, rowspan=len(info_rows), padx=10, pady=10
        )

        self.labels = {}
        self.string_vars = {}
        self.string_labels = {}
        for idx, (key, label) in enumerate(info_rows):
            l = tk.Label(self, text=label)
            l.grid(row=idx, column=1, sticky=tk.W)

            sv = tk.StringVar()
            sl = tk.Label(self, textvariable=sv)
            sl.grid_configure(row=idx, column=2, sticky=tk.W)

            self.labels[key] = l
            self.string_vars[key] = sv
            self.string_labels[key] = sl

    def update(self, user):
        img = get_user_image(user['avatar_url']).resize((230, 230))
        user_img = ImageTk.PhotoImage(img)

        self.img_label.configure(image=user_img)
        self.img_label.image = user_img

        for idx, (key, label) in enumerate(info_rows):
            text = user[key] if user[key] is not None else '(not provided)'
            if key != 'bio':
                self.string_vars[key].set(text)
            else:
                self.string_vars[key].set(insert_new_line(text))


class ErrorFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.label = tk.Label(
            self, text='Invalid User', fg='red', font=('Helvetica', 14, 'bold')
        )
        self.label.grid()


class Body(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.user_frame = UserContent(self)
        self.error_frame = ErrorFrame(self)

    def display_user(self, data):
        self.user_frame.update(data)
        self.user_frame.pack(fill='x', pady=10, padx=5)

    def display_error(self):
        self.error_frame.pack(pady=20)

    def hide(self):
        self.user_frame.pack_forget()
        self.error_frame.pack_forget()


class Footer(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.button = ttk.Button(
            self, text='Close', command=parent.close
        )
        self.button.grid(row=0, column=0)


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.header = Header(self, bg='white')
        self.header.pack(fill='x')

        self.searchbar = SearchBar(self)
        self.searchbar.pack(anchor='ne', pady=10, padx=5)

        self.body = Body(self)
        self.body.pack(fill='x', pady=10, padx=5)

        self.footer = Footer(self)
        self.footer.pack(anchor='se', expand=True, pady=5, padx=5)

    def close(self):
        return self.parent.destroy()

    def search(self, username):
        self.body.hide()

        user = get_user_details(username)
        if user:
            self.body.display_user(user)
        else:
            self.body.display_error()


def run_app():
    root = tk.Tk()

    app = MainApplication(root)
    app.pack(side='top', fill='both', expand=True)

    root.title('Github User Details')
    root.minsize(500, 200)
    root.mainloop()


if __name__ == '__main__':
    run_app()
