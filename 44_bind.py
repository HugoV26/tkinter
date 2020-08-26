from tkinter import *

root = Tk()
root.title('Tu nerd')
root.geometry("400x400")

def clicker(event):
    #myLabel = Label(root, text = "You clicked a button" + str(event.x) + " " + str(event.y))
    myLabel = Label(root, text = "You clicked a button" + event.char)
    myLabel.pack()

myButton = Button(root, text = "Click me")
#myButton.bind("<Button-1>", clicker)
#myButton.bind("<Enter>", clicker)
#myButton.bind("<Leave>", clicker)
#myButton.bind("<FocusIn>", clicker)
#myButton.bind("<Return>", clicker)
myButton.bind("<Key>", clicker)
myButton.pack(pady = 20)

root.mainloop()