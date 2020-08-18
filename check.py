from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Tu nerd')
root.geometry("400x400")


def show():
    myLabel = Label(root, text = var.get()).pack()

var = StringVar()

c = Checkbutton(root, text = "Check this", variable = var, onvalue = "On", offvalue = "Off")
c.deselect()
c.pack()



myButton = Button(root, text = "Show selection", command = show).pack()


root.mainloop()