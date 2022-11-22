# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Importing Libraries / Modules 
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
from PIL import Image # Imports PIL module 
import pytesseract # will convert the image to text string
import os # used to create folder and traverse directory paths and the files within
import datetime # used to get the date and time
import tkinter as tk # used to create the GUI
from tkinter import ttk

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Functions
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# --- Function to create output folder **
def makeDirectory(newDirectoryName):
    parentDirectory = "./"

    # merging parent path with desired new directory name
    path = os.path.join(parentDirectory, newDirectoryName)

    # creating directory
    os.mkdir(path)
    print("Directory '% s' created" % newDirectoryName)



# --- Function to open up an image and convert to text, pass in image path **
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

    with open(f'{outputFileToCreate}{originalPicName}.txt', 'a') as f:
        f.write(f"Text to Image Conversion - Run: {datetime.datetime.now()}") 
        f.write('\n')
        f.write(f"*** From Image: {originalPicName} *** ")
        f.write('\n')
        f.write(text)
        f.write('\n')


# --- Function to get input from user
def getInput(messageOnWhatToGet,errorMessage):
    outputFromUser = input(f"{messageOnWhatToGet}: ") # Main Output message
    while outputFromUser == '':
        outputFromUser = input(f'{errorMessage}: ') # Mesage if user enters nothing
    return outputFromUser


# --- Function to print out my Logo ---
def myLogo():
    print("Created and Tested by: ")
    print("   __                  _         ___ _                       ")
    print("   \ \  __ _  ___ ___ | |__     / __\ | ___  _   _ ___  ___  ")
    print("    \ \/ _` |/ __/ _ \| '_ \   / /  | |/ _ \| | | / __|/ _ \ ")
    print(" /\_/ / (_| | (_| (_) | |_) | / /___| | (_) | |_| \__ \  __/ ")
    print(" \___/ \__,_|\___\___/|_.__/  \____/|_|\___/ \__,_|___/\___| ")


"""
-=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=-
-=-=-=-=--=-=-=-=--=-=-=-=-       MAIN PROGRAM      -=-=-=-=--=-=-=-=--=-=-=-=-=
-=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=-
"""
# Storing Message: Creating Output Directory Name
createDirectoryMessage = 'Name the Output Directory'
createDirectoryMessageError = 'Name of directory can not be blank, enter a valid name'
directoryToCreate = getInput(createDirectoryMessage,createDirectoryMessageError)
print(directoryToCreate)
# Making Directory
makeDirectory(directoryToCreate)


# Storing Message: Creating Output File Name 
createOutputFileMessage = 'Output Filename to store converted text'
createOutputFileMessageError = 'Name of file can not be blank, enter a valid name'
outfileToCreate = getInput(createOutputFileMessage,createOutputFileMessageError)
# path to output directory - combine new directory and output name
outputPathAndFile = f"{directoryToCreate}/{outfileToCreate}"
print(outputPathAndFile)


# Storing Message: Getting Path to Image to Convert
getImgToConvertMessage = 'What is the relative path to the images you want to convert? (etc: "./Input/" - just the folder)'
getImgToConvertMessageError = 'Image path can not be blank. Enter valid path'
imageToConvert = getInput(getImgToConvertMessage,getImgToConvertMessageError)
# creating file
# with open(f'{outputPathAndFile}', 'w') as f:
#     f.write(f"Text to Image Conversion - Run: {datetime.datetime.now()}") 
#     f.write('\n')
#     f.write('\n')


# opening up folder and looping through images
for items in os.listdir(imageToConvert):
    print(items)
    convertToText(imageToConvert,outputPathAndFile,items)

# Print out my logo
myLogo()


'''

Created and tested by Jacob Clouse (with help with online sources as always in the README file)

'''