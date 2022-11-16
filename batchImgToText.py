# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Importing Libraries / Modules 
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
from PIL import Image # Imports PIL module 
import pytesseract # will convert the image to text string
import os # used to create folder and traverse directory paths and the files within
import datetime # used to get the date and time
import tkinter as tk # used to create the GUI


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Functions
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    # function to create output folder **
def makeDirectory(newDirectoryName):
    parentDirectory = "./"

    # merging parent path with desired new directory name
    path = os.path.join(parentDirectory, newDirectoryName)

    # creating directory
    os.mkdir(path)
    print("Directory '% s' created" % newDirectoryName)



    # function to open up an image and convert to text, pass in image path **
def convertToText(imagePath,outputFileToCreate,originalPicName):

    #Define path to tessaract.exe - Windows
    #path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    #Grabbing path to image from data being passed in
    path_to_image = f'{imagePath}/{originalPicName}'

    #Point tessaract_cmd to tessaract.exe - Windows
    #pytesseract.tesseract_cmd = path_to_tesseract

    #Open image with PIL
    img = Image.open(path_to_image)

    #Extract text from image
    text = pytesseract.image_to_string(img)

    with open(f'{outputFileToCreate}', 'a') as f:
        f.write('\n')
        f.write(f"*** From Image: {originalPicName} *** ")
        f.write('\n')
        f.write(text)
        f.write('\n')





"""
MAIN PROGRAM:
"""



import tkinter as tk

window = tk.Tk()

frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()

label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()

frame_a.pack()
frame_b.pack()

window.mainloop()


'''
# creating directory
directoryToCreate = input("Name the Output Directory: ")
while directoryToCreate == '':
    directoryToCreate = input("Name of directory can't be blank, enter a valid name: ") # won't accept blank for directory name
makeDirectory(directoryToCreate)


# getting output filename
outputFile = input("Output Filename to store converted text: ")
while outputFile == '':
    outputFile = input("Name of file can't be blank, enter a valid name: ") # won't accept blank for outputFile name



# path to output directory - combine new directory and output name
outputPathAndFile = f"{directoryToCreate}/{outputFile}.txt"

# getting image path
imageToConvert = input("What is the relative path to the images you want to convert: ") # etc: "./Input/ - just the folder
while imageToConvert == '':
    imageToConvert = input("Image path can't be blank. Enter valid path: ") # won't accept blank for path


# creating file
with open(f'{outputPathAndFile}', 'w') as f:
    f.write(f"Text to Image Conversion - Run: {datetime.datetime.now()}") 
    f.write('\n')
    f.write('\n')

# opening up folder and looping through images
for items in os.listdir(imageToConvert):
    print(items)
    convertToText(imageToConvert,outputPathAndFile,items)


'''