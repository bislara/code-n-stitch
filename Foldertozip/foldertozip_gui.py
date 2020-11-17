import zipfile, os, sys
import tkinter as tk
from tkinter import filedialog
from tkinter import CENTER, TOP, X

#Define default zip name
zipname = "zip"

# Zip function
def zipDir():
    global zipname
    if zip_name_area.get():
        zipname = zip_name_area.get()
    zipf = zipfile.ZipFile(f"{zipname}.zip", 'w', zipfile.ZIP_DEFLATED)
    abs_src = os.path.abspath(path)
    for root, dirs, files in os.walk(path):
        for file in files:
            absname = os.path.abspath(os.path.join(root,file))
            arcname = absname[len(abs_src)+1:]
            zipf.write(absname,arcname=arcname)
    zipf.close()
    
# Get folder path
def get_path():
    global path
    path = filedialog.askdirectory()
    zip_now_button["state"] = "normal"

#Gui
root=tk.Tk()
root.title("Foldertozip")

headingIcon = tk.Label(root, justify=CENTER, text="Zip Name")
headingIcon.pack(side=TOP, fill=X, padx=10)
#Zipname area
zip_name_area = tk.Entry(root,font=40)
zip_name_area.pack(side=TOP, fill=X, padx=10)

#Choose folder button
choose_folder_button = tk.Button(root,text="Choose Folder",font=40,command=get_path)
choose_folder_button.pack(side=TOP,padx=10,pady=10)

#Zipnow button
zip_now_button = tk.Button(root,text="Zip Now",font=40,command=zipDir)
zip_now_button.pack(side=TOP,padx=10,pady=10)

# Set zip_now_button state disabled for default
zip_now_button["state"] = "disabled"


root.mainloop()