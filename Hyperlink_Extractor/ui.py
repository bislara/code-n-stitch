from tkinter import *
from tkinter.ttk import Style
from links import get_links


class Ui:
    def __init__(self, master):
        self.master = master

        # App Title
        self.master.title("Link Extractor")

        # header_title
        self.header_title = Label(master, text="Extract links")
        self.header_title.grid(row=0, column=0)

        # input_text
        self.input_text = Text(master)
        self.input_text.grid(row=1, column=0)

        # out_label
        self.out_label = Label(master, text="Output")
        self.out_label.grid(row=0, column=1)

        # out_text
        self.out_text = Text(master)
        self.out_text.grid(row=1, column=1)

        # generate_button
        self.generate_button = Button(master, text="Generate", command=self.generate)
        self.generate_button.grid(row=2, column=0, columnspan=2)

    def generate(self):
        self.out_text.delete(1.0, END)
        self.out_text.insert(END, "\n".join(get_links(self.input_text.get(1.0, END))))


def quit_():
    exit()


# App Theme
def run_gui():
    root = Tk()
    root.style = Style()
    root.style.theme_use("default")
    Ui(root)
    root.mainloop()


if __name__ == "__main__":
    run_gui()
