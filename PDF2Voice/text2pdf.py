#there are many inbuilt packages that convert the pdf to text like Py2PDF, tika etc, but when tested on pdfs where the metadata is an image they fail.
#pdf2text and pytesseract whereas generates the text file for such pdfs as well, these generated outputs can be further used for other purposes like OCR etc.

import pandas as pd
import pytesseract as pts
import pdf2image
from gtts import gTTS 
import argparse


#pdf to text 

def pdf2text(args):

	pages = pdf2image.convert_from_path(pdf_path=args.input, dpi=args.dpi, size= tuple(args.size))
	# Save all pages as images
	print(len(pages))
	for i in range(0,len(pages)):
		pages[i].save("pages/"+ "page_"+ str(i) + '.jpg')
	return pages


#conversion of the images generated out of the pdf

def text2speech(pages,args):

	for i in range(len(pages)):
		content = pts.image_to_string(pages[0], lang="swe")
		myobj = gTTS(text=content, lang=language, slow=False) 
		myobj.save(args.output + "page_" + str(i)+".mp3") 
  
  		#to play the following audio file 
		# os.system("mpg321 args.output + "page_" + str(i)+".mp3") 


parser = argparse.ArgumentParser(description="PDF2Speech simple script")

parser.add_argument('--input', help='an input pdf file to read', required = True)
parser.add_argument('--dpi',help='dpi', type=int, required=True)
parser.add_argument('--size', nargs=2, type=int, help='size of the image to be generated', required=True)
parser.add_argument('--output', help='output path of the pagewise audio', required=True)

args = parser.parse_args()

language = "en"
text2speech(pdf2text(args),args)