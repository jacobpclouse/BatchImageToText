# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Importing Libraries / Modules 
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
from PIL import Image # Imports PIL module 
import pytesseract # will convert the image to text string


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Functions
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    # function to create output folder


    # function to open up an image and convert to text
def convertToText():

    #Define path to tessaract.exe
    path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    #Define path to image
    path_to_image = 'sample2.png'

    #Point tessaract_cmd to tessaract.exe
    pytesseract.tesseract_cmd = path_to_tesseract

    #Open image with PIL
    img = Image.open(path_to_image)

    #Extract text from image
    text = pytesseract.image_to_string(img)
    print(text)




"""
MAIN PROGRAM:
"""
convertToText()