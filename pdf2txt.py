import sys
import tempfile
import pytesseract
from pathlib import Path
from PIL import Image
from pdf2image import convert_from_path

# largely inspired by:
# https://www.geeksforgeeks.org/python-reading-contents-of-pdf-using-ocr-optical-character-recognition/

pdfs = Path('.').glob('*.pdf')
for pdf in pdfs:
    outfile = pdf.stem + '.txt'
    print(f'Converting {pdf} to {outfile}')

    with tempfile.TemporaryDirectory() as temp_folder, open(outfile, 'w+') as text_file:
        # convert PDFs at high DPI for maximum accuracy
        pages = convert_from_path(pdf, dpi=300, output_folder=temp_folder)

        # use OCR to extract text from each page image
        page_count = 0
        for page in pages:
            page_count += 1
            sys.stdout.write(f'\r  Converting page {page_count} of {len(pages)}')

            # write image to disk
            image_path = Path(temp_folder) / Path(f'page_{page_count}.jpg')
            page.save(str(image_path), 'JPEG')

            # convert to text
            text = pytesseract.image_to_string(Image.open(str(image_path)))
            text_file.write(text)

    print()