from csv import writer
from pathlib import Path
from PyPDF2 import PdfFileMerger, PdfFileReader
import sys
import os


# Define input directory for the pdf files
pdf_dir = Path(__file__).parent / "to_convert"

# The output directory.
pdf_output_dir = Path(__file__).parent / "converted"
pdf_output_dir.mkdir(parents=True, exist_ok=True)

# To take the list of all the .pdf files
pdf_files = list(pdf_dir.glob("*.pdf"))

# Use the first 3 characters as the 'key'
keys = set([file.name[:3] for file in pdf_files])

# Determine the file name length of the base file

BASE_FILE_NAME_LENGTH = 20

for key in keys:
    merger = PdfFileMerger()
    for file in pdf_files:
        if file.name.startswith(key):
            merger.append(PdfFileReader(str(file), "rb"))
            if len(file.name) >= BASE_FILE_NAME_LENGTH:
                base_file_name = file.name
    merger.write(str(pdf_output_dir / base_file_name))
    merger.close()