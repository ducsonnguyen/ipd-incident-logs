# IPD Incident Log Tools
Ithaca Police Department's incident logs are exported in image-only (non-searchable, non-selectable) PDFs. These are scripts to download logs and use OCR to extract text from them.

# Setup (Ubuntu)
Install these apt packages:

    sudo apt install cmake libleptonica-dev libtesseract-dev tesseract-ocr poppler-utils

Install these pip packages

    sudo pip3 install beautifulsoup4 requests pytesseract pdf2image tesseract-ocr Pillow

# Run
Run `get-logs.py` to download the latest from IPD's incident logs website:

    python3 get-logs.py

Run `pdf2txt.py` to iterate through PDFs and extract text from them via OCR:

    python3 pdf2txt.py

# TODO
Clean up formatting, convert to csv
