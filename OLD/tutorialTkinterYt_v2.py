# https://www.youtube.com/watch?v=BSfbjrqIw20&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=2
from tkinter import *

root = Tk()
e = Entry(root, width=50)
e.grid(row=1,column=0)
e.insert(0, "Enter your name: ")

""" FUNCTIONS """
def myClick():
    inputStore = 'Hi there: ' + e.get()
    myLabel = Label(root, text=inputStore)
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