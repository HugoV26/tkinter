from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Tu nerd')
root.geometry("400x400")

def comboclick(event):
    #myLabel = Label(root, text = myCombo.get()).pack()
    if myCombo.get() == "Friday":
        myLabel = Label(root, text = "Yes, lets get drunk").pack()
    else:
        myLabel = Label(root, text = myCombo.get()).pack()


def selected(event):
    #myLabel = Label(root, text = clicked.get()).pack()
    if clicked.get() == "Friday":
        myLabel = Label(root, text = "Yes, lets get drunk").pack()
    else:
        myLabel = Label(root, text = clicked.get()).pack()

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options, command = selected)
drop.pack(pady = 20)

myCombo= ttk.Combobox(root, value = options)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", comboclick)
myCombo.pack()

#myButton = Button(root, text = "Select from list", command = selected)
#myButton.pack()

root.mainloop()