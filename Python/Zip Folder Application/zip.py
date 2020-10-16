import shutil, os
from tkinter import *
from tkinter import filedialog

# Default Zipped Folder Name (If the user selects no name, use this)
zipname = "zipped_folder"

# Define function to allow the user to browse to find a folder to zip
def browse():
    global pathname 
    current_path = os.path.abspath(os.getcwd())
    currentPath.config(text=current_path)
    pathname = filedialog.askdirectory()
    pathlabel.config(text=pathname)
    zipButton["state"] = "normal"

# Define function to zip the selected folder
def zipFolder():
    global zipname
    if zip_name_area.get():
        zipname = zip_name_area.get()
    shutil.make_archive(zipname, 'zip', pathname)

app = Tk()

browsebutton = Button(app, text="Browse", command=browse, fg="#708090", bg="white" ,font=("Helvetica", 14, "bold"))
browsebutton.grid(row=1,column=1, pady=20, padx=10, sticky=W)

# Path of the selected File Name
boxLabel = Label(app, text="Path Of The Folder Selected", fg="white", bg="#708090" ,font=("Helvetica", 12, "bold"))
boxLabel.grid(row=1,column=2, padx=10, sticky=W)

# Displays the path of the selected file
pathlabel = Label(app, fg="white", bg="#708090" ,font=("Helvetica", 12, "bold"))
pathlabel.grid(row=1,column=2, padx=5, sticky=W)

# Zipname Field 
zip_label = Label(app,text="Enter Zip Name", fg="white", bg="#708090" ,font=("Helvetica", 12, "bold"))
zip_label.grid(row=2, column=1, padx=10, pady=20, sticky=W, columnspan=2)

# Zipname Label
zip_name_area = Entry(app,font=14)
zip_name_area.grid(row=2, column=2, padx=10, pady=20, sticky=W)

# Zip Button
zipButton = Button(app, text="Zip Folder", command=zipFolder, fg="#708090", bg="white" ,font=("Helvetica", 14, "bold"))
zipButton.grid(row=3,column=1, pady=20, padx=10, sticky=W)

# Zip Path Label
boxLabel2 = Label(app, text="Path Zip Has Been Saved To", fg="white", bg="#708090" ,font=("Helvetica", 12, "bold"))
boxLabel2.grid(row=3,column=2, padx=10, sticky=W, columnspan=2)

# Zip Path
currentPath = Label(app, text="Path Zip Has Been Saved To", fg="white", bg="#708090" ,font=("Helvetica", 12, "bold"))
currentPath.grid(row=3,column=2, padx=10, sticky=W)

# Set zip_now_button state disabled for default
zipButton["state"] = "disabled"

app.title("Zip FIle")
app.configure(bg='#708090')

app.mainloop()
