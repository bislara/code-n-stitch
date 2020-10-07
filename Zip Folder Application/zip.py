import shutil
import os
import tkinter as Tk
from tkinter import filedialog


app = Tk()

def browse():
    current_path = os.path.abspath(os.getcwd())
    currentPath.config(text=current_path)
    pathname = filedialog.askdirectory()
    name = pathname.split('/')
    filename = name[-1] 
    pathlabel.config(text=pathname)
    shutil.make_archive(filename, 'zip', pathname)

browsebutton = Button(app, text="Find & Zip Folder", command=browse, font=("bold", 14),)
browsebutton.grid(row=0,column=2, pady=20, padx=40)

# Path of the selected File
boxLabel = Label(app, text="Path Of The Folder Selected")
boxLabel.grid(row=1,column=2, padx=40)
pathlabel = Label(app)
pathlabel.grid(row=2,column=2, padx=40)

boxLabel2 = Label(app, text="Path Zip Has Been Saved To")
boxLabel2.grid(row=3,column=2, padx=40)
currentPath = Label(app)
currentPath.grid(row=4,column=2, padx=40)


app.title("Zip FIle")
app.geometry("250x180")
app.configure(bg='#708090')

app.mainloop()