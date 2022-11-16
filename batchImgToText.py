# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Importing Libraries / Modules 
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
from PIL import Image # Imports PIL module 
import pytesseract # will convert the image to text string


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Functions
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    # function to create output folder


    # function to open up an image and convert to text, pass in image path
def convertToText(imagePath):

    #Define path to tessaract.exe - Windows
    #path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    #Grabbing path to image from data being passed in
    path_to_image = f'{imagePath}'

    #Point tessaract_cmd to tessaract.exe - Windows
    #pytesseract.tesseract_cmd = path_to_tesseract

    #Open image with PIL
    img = Image.open(path_to_image)

    #Extract text from image
    text = pytesseract.image_to_string(img)
    print(text)




"""
MAIN PROGRAM:
"""
imageToConvert = input("What is the path to the image: ") # etc: "./Input/sample2.png"
convertToText(imageToConvert)