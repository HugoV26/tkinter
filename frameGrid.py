from tkinter import *

root = Tk()

frameOne = Frame(root, borderwidth = 2, pady = 2).grid(row = 0, column = 0)

header = Label(frameOne, text = "Test Frame", bg = 'blue', fg = "white", height = 3, width = '50', font = ("Helvetica 16 bold")).grid(row = 0, column = 0)

root.mainloop()