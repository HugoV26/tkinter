from tkinter import *

root = Tk()
root.title('Tu nerd')
root.geometry("800x800+500+500")

def resize():
    w = widthEntry.get()
    h = heightEntry.get()
    pr = posRightEntry.get()
    pd = posDownEntry.get()
    root.geometry(f"{w}x{h}+{pr}+{pd}")
    #root.geometry(f"{w}x{h}".format(width = w, height = h))
    #root.geometry("%ix%i" % (w, h))

widthLabel = Label(root, text = "Width: ")
widthLabel.pack(pady = 20)
widthEntry = Entry(root)
widthEntry.pack()

heightLabel = Label(root, text = "Height: ")
heightLabel.pack(pady = 20)
heightEntry = Entry(root)
heightEntry.pack()

posRightLabel = Label(root, text = "Position Right: ")
posRightLabel.pack(pady = 20)
posRightEntry = Entry(root)
posRightEntry.pack()

posDownLabel = Label(root, text = "Position Down: ")
posDownLabel.pack(pady = 20)
posDownEntry = Entry(root)
posDownEntry.pack()


myButton = Button(root, text = "Resize", command = resize)
myButton.pack(pady = 20)


root.mainloop()