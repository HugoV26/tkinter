from tkinter import *

root = Tk()

e = Entry(root, width = 50, fg = "green", bg = "yellow", borderwidth=50)
e.pack()
#e.get()
e.insert(0, "Enter your name: ")


def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

#myButton = Button(root, text="Click me", padx=50, pady=50)
myButton = Button(root, text="Enter your name", command=myClick, fg="blue", bg="black", borderwidth=10)
myButton.pack()


root.mainloop()