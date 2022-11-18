# https://www.youtube.com/watch?v=BSfbjrqIw20&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=2
from tkinter import *

root = Tk()

# Input Existing File Path input
filePath = Entry(root, width=50, borderwidth=5)
filePath.pack()

# New File Name input
newFileName = Entry(root, width=50, borderwidth=5)
newFileName.pack()

# New Directory input
newDirectoryName = Entry(root, width=50, borderwidth=5)
newDirectoryName.pack()


""" FUNCTIONS """
# Function for GUI
def myClick():
    # getting label content
    filePathGET = filePath.get()
    newFileNameGET = newFileName.get()
    newDirectoryNameGET = newDirectoryName.get()
    
    # fixing labels
    filePathLabel = Label(root, text=filePathGET)
    newFileNameLabel2 = Label(root, text=newFileNameGET)
    newDirectoryNameLabel3 = Label(root, text=newDirectoryNameGET)

    # Packing Labels
    filePathLabel.pack()
    newFileNameLabel2.pack()
    newDirectoryNameLabel3.pack()
    print(f"{filePathGET} and {newFileNameGET} and {newDirectoryNameGET}")
    



# buttons
myButton = Button(root, text="Click ME!", command=myClick, fg="white", bg="black")
myButton.pack()




root.mainloop()