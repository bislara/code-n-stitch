import os
import typer
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from PyPDF2 import PdfFileReader, PdfFileWriter

FILE_IN = ''
FILE_OUT = ''


def watermarking(input_path: str, watermark_path: str, output_path:str):
    # Detecting if watermark is img or pdf
    if watermark_path.endswith('.pdf'):
        watermark = PdfFileReader(watermark_path).getPage(0)
    else:
        img_temp = BytesIO()
        image_watermark = ImageReader(watermark_path)
        new_canvas = canvas.Canvas(img_temp, pagesize=letter)
        new_canvas.drawImage(image_watermark, 90, 200, 400, 400, mask='auto')
        new_canvas.save()
        watermark = PdfFileReader(BytesIO(img_temp.getvalue())).getPage(0)
    
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