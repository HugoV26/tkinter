from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!")
    myLabel.pack()

#myButton = Button(root, text="Click me", padx=50, pady=50)
myButton = Button(root, text="Click me!", command=myClick, fg="blue", bg="black")
myButton.pack()


root.mainloop()