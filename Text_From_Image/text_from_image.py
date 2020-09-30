#To extract text from the image we can use the PIL and pytesseract libraries
from PIL import Image
import PIL.Image

from pytesseract import image_to_string
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract' #path location of library
TESSDATA_PREFIX = 'C:/Program Files (x86)/Tesseract-OCR'
output = pytesseract.image_to_string(PIL.Image.open('Image1.PNG').convert("RGB"), lang='eng')
print output
