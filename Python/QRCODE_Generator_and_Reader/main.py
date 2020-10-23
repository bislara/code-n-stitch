import pyqrcode
import png
from imutils.video import VideoStream
import imutils
from pyzbar.pyzbar import decode
from PIL import Image
import time
import tkinter
from tkinter import ttk
from tkinter import filedialog

# Defining the functions

def generate(): # Called to generate a qrcode
    text = Inputbox.get("1.0","end")
    path = filedialog.asksaveasfilename(title="Save QRCODE", filetypes = (("Png file", "*.png"),))
    QRcode = pyqrcode.create(text)
    QRcode.png(path, scale=8)
    Inputbox.delete("1.0","end")

def browse(): # Called to read qrcode from file
    Outputbox.delete("1.0","end")
    path = filedialog.askopenfilename(title="Open file", filetypes = (("Image files", "*.*"),))
    barcodes = decode(Image.open(path))
    try:
        Outputbox.insert("1.0", barcodes[0].data.decode())
    except:
        pass

def webcam(): # Called to read qrcode from webcam
    vs = VideoStream(src=0).start()
    time.sleep(2.0)
    barcodes = []
    while not barcodes:
        frame = vs.read()
        frame = imutils.resize(frame, width=400)

        barcodes = decode(frame)
    vs.stop()
    Outputbox.insert("1.0", barcodes[0].data.decode())


# Creating the window
root = tkinter.Tk()
root.title("QRCODE Generator and scanner")


# Setting up the notebook
Main_notebook = ttk.Notebook(root)
Main_notebook.pack()


# Making the frames
Generator_frame = tkinter.Frame(Main_notebook)
Generator_frame.pack(fill="both", expand=1)
Main_notebook.add(Generator_frame, text="Generator")

Scanner_frame = tkinter.Frame(Main_notebook)
Scanner_frame.pack(fill="both", expand=1)
Main_notebook.add(Scanner_frame, text="Scanner")


# Making the generator frame
Generator_instructions = tkinter.Label(Generator_frame, text="Usage instructions-\n1. Enter the text to be converted in the box.\n2. Click on the generate button and choose a output location")
Generator_instructions.pack()

Generate_button = tkinter.Button(Generator_frame, text="Generate", command=generate)
Generate_button.pack()

Inputbox = tkinter.Text(Generator_frame)
Inputbox.pack()


# Making the scanner frame
Scanner_instructions = tkinter.Label(Scanner_frame, text="Usage instructions-\n1. If you want to read qrcode from file then use the browse button.\n2. If you want to read from webcam then use the webcam button.\n3. The result will be displayed in the text box below.")
Scanner_instructions.pack()

Browse_button = tkinter.Button(Scanner_frame, text="Browse", command=browse)
Browse_button.pack()

Webcam_button = tkinter.Button(Scanner_frame, text="Webcam", command=webcam)
Webcam_button.pack()

Outputbox = tkinter.Text(Scanner_frame)
Outputbox.pack()


# Creating the main loop
root.mainloop()