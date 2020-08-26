from tkinter import *

root = Tk()
root.title('Tu nerd')
root.geometry("400x400")

class Itachi:

    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()

        self.myButton = Button(master, text = "Cick me!", command = self.clicker)
        self.myButton.pack(pady = 20)

    def clicker(self):
        print("You clicked a button")


e = Itachi(root)



root.mainloop()