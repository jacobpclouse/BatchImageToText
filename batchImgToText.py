# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Importing Libraries / Modules 
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# from PIL import Image # Imports PIL module 
import PIL.Image
import pytesseract # will convert the image to text string
import os # used to create folder and traverse directory paths and the files within
import datetime # used to get the date and time
from tkinter import * # used to create the GUI


""" TKINTER SETUP """
root = Tk()
root.title('GUI Batch Image Converter')


# Input Existing File Path input
labelFilePath = Label(root, text="Enter File Path: ") # label
labelFilePath.pack()
filePath = Entry(root, width=50, borderwidth=5) # entry
filePath.pack()

# New File Name input
labelNewFileName = Label(root, text="Enter New Output File Name: ") # label
labelNewFileName.pack()
newFileName = Entry(root, width=50, borderwidth=5) # entry
newFileName.pack()

# New Directory input
labelNewDirectoryName = Label(root, text="Enter New Directory Name: ") # label
labelNewDirectoryName.pack()
newDirectoryName = Entry(root, width=50, borderwidth=5) # entry
newDirectoryName.pack()
''' End of TKINTER SETUP '''

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
    # img = Image.open(path_to_image)
    img = PIL.Image.open(path_to_image)
    # img.show()

    #Extract text from image
    text = pytesseract.image_to_string(img)

    with open(f'{outputFileToCreate}', 'a') as f:
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


# Function for GUI
def myClick():

    # getting label content
    imageToConvert = filePath.get()
    outfileToCreate = newFileName.get()
    directoryToCreate = newDirectoryName.get()
    
    # fixing labels
    filePathLabel = Label(root, text=imageToConvert)
    newFileNameLabel2 = Label(root, text=outfileToCreate)
    newDirectoryNameLabel3 = Label(root, text=directoryToCreate)

    # Packing Labels
    filePathLabel.pack()
    newFileNameLabel2.pack()
    newDirectoryNameLabel3.pack()

# PROCESSING
    # Making Directory
    makeDirectory(directoryToCreate)

    # path to output directory - combine new directory and output name
    outputPathAndFile = f"{directoryToCreate}/{outfileToCreate}.txt"
    # creating clean file
    with open(f'{outputPathAndFile}', 'w') as f:
        f.write(f"Text to Image Conversion - Run: {datetime.datetime.now()}") 
        f.write('\n')
        f.write('\n')    


    # opening up folder and looping through images
    for items in os.listdir(imageToConvert):
        print(items)
        convertToText(imageToConvert,outputPathAndFile,items)


    print(f"Input File path: {imageToConvert} \n  Output File to create: {outfileToCreate}.txt \n Output Directory to create: {directoryToCreate}")
    # Print out my logo
    myLogo()
"""
-=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=-
-=-=-=-=--=-=-=-=--=-=-=-=-       MAIN PROGRAM      -=-=-=-=--=-=-=-=--=-=-=-=-=
-=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=--=-=-=-=-
"""


'''
# Storing Message: Creating Output Directory Name
createDirectoryMessage = 'Name the Output Directory'
createDirectoryMessageError = 'Name of directory can not be blank, enter a valid name'

# Storing Message: Creating Output File Name 
createOutputFileMessage = 'Output Filename to store converted text'
createOutputFileMessageError = 'Name of file can not be blank, enter a valid name'

# Storing Message: Getting Path to Image to Convert
getImgToConvertMessage = 'What is the relative path to the images you want to convert? (etc: "./Input/" - just the folder)'
getImgToConvertMessageError = 'Image path can not be blank. Enter valid path'

directoryToCreate = getInput(createDirectoryMessage,createDirectoryMessageError)
print(directoryToCreate)

outfileToCreate = getInput(createOutputFileMessage,createOutputFileMessageError)

print(outputPathAndFile)

imageToConvert = getInput(getImgToConvertMessage,getImgToConvertMessageError)

'''
# buttons
myButton = Button(root, text="Click ME!", command=myClick, fg="white", bg="black")
myButton.pack()




root.mainloop()
'''

Created and tested by Jacob Clouse (with help with online sources as always in the README file)

'''