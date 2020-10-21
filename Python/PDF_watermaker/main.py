import os
import typer
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from PIL import Image 
from PyPDF2 import PdfFileReader, PdfFileWriter

FILE_IN = ''
FILE_OUT = ''

def transparency(image, alpha= 125):
    newData = []
    for item in image:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            if any(i< 20 for i in item[:3]):
                newData.append(item)
            else:
                newData.append((item[0],item[1],item[2],alpha))
    return newData

def watermarking(input_path: str, watermark_path: str, output_path:str):
    # Detecting if watermark is img or pdf
    if watermark_path.endswith('.pdf'):
        watermark = PdfFileReader(watermark_path).getPage(0)
    else:
        img = BytesIO()
        image_watermark = Image.open(watermark_path).convert('RGBA')
        new_data = transparency(image_watermark.getdata())
        image_watermark.putdata(new_data)
        image_watermark.save(img, 'PNG')
        new_img = ImageReader(img)        
        img_doc = BytesIO()
        new_canvas = canvas.Canvas(img_doc, pagesize=letter)
        new_canvas.drawImage(new_img, 90, 200, 400, 400, mask='auto')
        new_canvas.save()
        watermark = PdfFileReader(BytesIO(img_doc.getvalue())).getPage(0)
    
    pdf_in = PdfFileReader(input_path)
    pdf_out = PdfFileWriter()
    
    #Iterating on pages ading to each one
    for page_num in range(pdf_in.getNumPages()):
        page = pdf_in.getPage(page_num)
        page.mergePage(watermark)
        pdf_out.addPage(page)

    with open(output_path, 'wb') as output:
        pdf_out.write(output)   

def main(input: str, watermark: str, output: str = ''):
    if not os.path.isfile(input) or not os.path.isfile(watermark):
        raise Exception('File {} or {} does not exist.'.format(input, watermark))
    if not input.lower().endswith('.pdf'):
        raise Exception('File type is not an pdf')
    if not watermark.lower().endswith(('.png', '.jpg', '.jpeg', '.pdf')):
        raise Exception('File type is not an image or pdf')
    FILE_IN = input

    if output != '':
        FILE_OUT = output
    else:
        new_path = input.split('.')
        new_path[-2] += '-watermaked'
        FILE_OUT = '.'.join(new_path)
    print(FILE_OUT)
    watermarking(FILE_IN, watermark, FILE_OUT)

if __name__ == "__main__":
    typer.run(main)