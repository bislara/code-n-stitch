import tkinter as tk 
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import re

email_regex = re.compile(r"[\w\.-]+@[\w\.-]+")
phone_num_regex = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# url_regex = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")
url_regex_https = re.compile(r"https?://www\.?\w+\.\w+")
url_regex = re.compile(r"http?://www\.?\w+\.\w+")

window = Tk()
window.title("Email Extractor")
window.geometry('700x500')

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1,text="Home")

tab_control.pack(expand=1,fill='both')


label1 = Label(tab1, text= 'Email EXTRACTOR',padx=5, pady=5)
label1.grid(column=0, row=0)
 


# Clear entry widget

def clear_text():
	entry1.delete('1.0',END)

def clear_text_url():
	entry.delete('1.0',END)

def clear_display_result():
	tab1_display.delete('1.0',END)

def clear_display_result_url():
	tab2_display.delete('1.0',END)

def extract_email():
	raw_text = str(entry1.get('1.0',tk.END))
	final_extract = email_regex.findall(raw_text)
	num_of_results = len(final_extract)
	result = '\nNumber of Emails:{},\nEmails:{}'.format(num_of_results,final_extract)
	tab1_display.insert(tk.END,result)

 

# Main Page
l1=Label(tab1,text="Enter Text To Extract")
l1.grid(row=1,column=0)

entry1=ScrolledText(tab1,height=10)
entry1.grid(row=2,column=0,columnspan=2,padx=5,pady=5)

# BUTTONS
button_1=Button(tab1,text="Reset",command=clear_text, width=10,bg='#03A9F4',fg='#fff')
button_1.grid(row=4,column=0,padx=10,pady=10)

button_2=Button(tab1,text="Email",command=extract_email, width=10,bg='red',fg='#fff')
button_2.grid(row=4,column=1,padx=10,pady=10)

# Display Screen For Result
tab1_display = ScrolledText(tab1,height=10)
tab1_display.grid(row=7,column=0, columnspan=3,padx=5,pady=5)


# URL Page Page
l1=Label(tab2,text="Enter Text To Extract Links")
l1.grid(row=1,column=0)

entry=ScrolledText(tab2,height=10)
entry.grid(row=2,column=0,columnspan=2,padx=5,pady=5)

# BUTTONS
button1=Button(tab2,text="Reset",command=clear_text_url, width=10,bg='#03A9F4',fg='#fff')
button1.grid(row=4,column=0,padx=10,pady=10)

button2=Button(tab2,text="Extract EMAIL",command=extract_email, width=10,bg='red',fg='#fff')
button2.grid(row=4,column=1,padx=10,pady=10)





# Display Screen For Result
tab2_display = ScrolledText(tab2,height=10)
tab2_display.grid(row=7,column=0, columnspan=3,padx=5,pady=5)




window.mainloop()