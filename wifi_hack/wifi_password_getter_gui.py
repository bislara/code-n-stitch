# This is a simple GUI version for wifi_password_getter.py script.
# To run, open terminal in present directory and simply type - python wifi_password_getter.py


from tkinter import *
from wifi_password_getter import getWifiPasswords

# GLOBALS
root=Tk()
width=480
height=320

#GUI Logic
root.geometry(str(width)+"x"+str(height))
root.minsize(width,height)
root.maxsize(width,height)
root.title("Wifi Password Getter")

logo=PhotoImage(file="images/wifi.png")
logo = logo.subsample(2, 2)

logo_label=Label(image=logo)
logo_label.place(x=0, y=0, relwidth=1, relheight=1)

fetch_button=Button(text ="Fetch", command = getWifiPasswords)
fetch_button.pack()

root.mainloop()