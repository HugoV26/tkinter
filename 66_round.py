from tkinter import *

root = Tk()
root.title('Tu nerd')
root.geometry("400x400")

def some():
    myLabel.config(text = "You cliked the button...")

englishButton = PhotoImage(file = 'images/lupa.png') 


imgLabel = Label(image = englishButton)
#imgLabel.pack(pady = 20)


myButton = Button(root, image = englishButton, command = some, borderwidth = 0)
myButton.pack(pady = 20)

myLabel = Label(root, text = ' ')
myLabel.pack(pady = 20)
root.mainloop()