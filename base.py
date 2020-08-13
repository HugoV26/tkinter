from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Tu Nerd')

def open():
    global my_img
    top = Toplevel()
    top.title('Tu Nerd Top')
    my_img = ImageTk.PhotoImage(Image.open("images/image3.png"))
    #lbl = Label(top, text = "Hey...").pack()
    my_label = Label(top, image = my_img).pack()
    btn2 = Button(top, text = "Close windows", command = top.destroy).pack()


btn = Button(root, text = "Open Second Window", command = open).pack()

root.mainloop()

#60:38:E0:91:94:C8
