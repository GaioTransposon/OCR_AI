#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 15:18:15 2024

@author: dgaio
"""

import fitz  # PyMuPDF

def extract_images_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    images = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        image_list = page.get_images(full=True)
        for image_index, img in enumerate(page.get_images(full=True)):
            base_image = doc.extract_image(img[0])
            image_bytes = base_image["image"]
            images.append(image_bytes)
    return images



import pytesseract
from PIL import Image
import io

# Assuming `extract_images_from_pdf` is defined as above

pdf_path = '/Users/dgaio/cloudstor/Gaio/topo documenti/sanità/20231214_Gaio_analisi.pdf'
images = extract_images_from_pdf(pdf_path)

for img_bytes in images:
    image = Image.open(io.BytesIO(img_bytes))
    text = pytesseract.image_to_string(image)
    print(text)
