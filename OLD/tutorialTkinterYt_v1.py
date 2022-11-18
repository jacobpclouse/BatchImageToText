# https://www.youtube.com/watch?v=BSfbjrqIw20&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=2
from tkinter import *

root = Tk()

""" FUNCTIONS """
def myClick():
    myLabel = Label(root, text="In a button boi")
    myLabel.grid(row=0,column=0)


#labels
# myLabel1 = Label(root, text="Hello world!")
# myLabel2 = Label(root, text="My Name is Jacob Clouse")

# myLabel1.grid(row=0,column=0)
# myLabel2.grid(row=1,column=0)


# buttons
myButton = Button(root, text="Click ME!", command=myClick, fg="white", bg="black")
myButton.grid(row=1,column=1)

root.mainloop()