from tkinter import Tk, Label, Text, Button, END, Listbox, Scrollbar, messagebox
from link_checker import find_broken_links

if __name__ == '__main__':
    window = Tk()
    window.title("Website broken link finder")
    window.geometry('500x300')

    url_input_label = Label(window, text="Enter base URL:")
    url_input_label.grid(column=0, row=0)

    url_input = Text(window, height=1, width=40)
    url_input.grid(column=1, row=0)

    listbox_label = Label(window, text="Broken links:")
    listbox_label.grid(column=0, row=1)

    #Results listbox
    listbox = Listbox(window, width=40)
    listbox.grid(column=0, row=2, columnspan=2)
    scrollbar = Scrollbar(window)
    scrollbar.grid(column=2, row=2)

    listbox.insert(END, "Broken links here")

    #Attaching scrollbar to listbox and setting vertical scroll
    listbox.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = listbox.yview)

    def check_website(address):
        """Obtains broken links from input address and repopulates listbox"""
        broken_links = find_broken_links(address)
        listbox.delete(0,'end')
        if len(broken_links) > 0:
            for broken_link in broken_links:
                listbox.insert(END, broken_link)
        else:
            listbox.insert(END, "No broken links!")

        messagebox.showinfo('Status','Broken links obtained!')


    btn = Button(window, text="Find broken links", command=lambda: check_website(url_input.get("1.0","end-1c")))
    btn.grid(column=2, row=0)

    window.mainloop()
