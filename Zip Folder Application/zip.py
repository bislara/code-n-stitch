import shutil
import os
import tkinter as Tk
from tkinter import filedialog


app = Tk() 

# Defines a function for the user to be able to select the folder they wish to Zip
def browse():
    current_path = os.path.abspath(os.getcwd()) # Gets the current path of the application
    currentPath.config(text=current_path) # Appends the current path to the currentPath label
    pathname = filedialog.askdirectory() 
    name = pathname.split('/') # Splits the pathname on "/" 
    filename = name[-1] # Gets the name of the folder selected from the pathname (The last section of the path)
    pathlabel.config(text=pathname) # Appends the pathname to the pathlabel label
    shutil.make_archive(filename, 'zip', pathname)

browsebutton = Button(app, text="Find & Zip Folder", command=browse, font=("bold", 14),) # Sets up the button for finding the folder to Zip
browsebutton.grid(row=0,column=2, pady=20, padx=40)

# Sets up the labels & selection boxes
boxLabel = Label(app, text="Path Of The Folder Selected")
boxLabel.grid(row=1,column=2, padx=40)
pathlabel = Label(app)
pathlabel.grid(row=2,column=2, padx=40)

boxLabel2 = Label(app, text="Path Zip Has Been Saved To")
boxLabel2.grid(row=3,column=2, padx=40)
currentPath = Label(app)
currentPath.grid(row=4,column=2, padx=40)

# Sets up the application title, background colour and window size
app.title("Zip FIle")
app.geometry("250x180")
app.configure(bg='#708090')

app.mainloop()
