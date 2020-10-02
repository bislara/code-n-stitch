try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from tkinter import *
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText

# Setup the window and make the title
root = Tk() 
root.title("Text from image(OCR)")

# Defining the functions
def ocr(Path_to_image):
    '''
    This function converts images into text and returns a string with whitespace stripped off
    '''

    return pytesseract.image_to_string(Path_to_image).strip()

def browse(): # Called when person hits browse
    Output_box.delete(1.0,END)
    Output_box.insert(INSERT,ocr(filedialog.askopenfilename(initialdir="~/", title="Please select image", filetypes = (("Image files","*.jpg"),("Image files","*.jpeg"),("Image files","*.bmp"),("Image files","*.pnm"),("Image files","*.png"),("Image files","*.jfif"),("Image files","*.tiff"),("Image files","*.tif")))))

# Make all the widgets
Instructions = Label(root,text="Click on browse button and select the image that you\nwant to scan. (You can also edit the output to fix any mistakes)")
Browse_button = Button(root, text="Browse", command=browse)
Output_box = ScrolledText(root)

# Place the widgets
Instructions.pack()
Browse_button.pack()
Output_box.pack()

# Start the application
root.mainloop()