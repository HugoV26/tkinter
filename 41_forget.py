from tkinter import *

root = Tk()
root.title('Tu nerd')
root.geometry("400x400")

def myDelete():
    #if mylabeLl8.winfo_exists() == 1:
    #    print("do some")
    #else:
    #    print("do some")
    #myLabel8.pack_forget()
    myLabel8.destroy()
    myButton['state'] = NORMAL
    print(myButton.winfo_exists())

def myClick():
    global myLabel8
    hello = "Hello " + e.get()
    myLabel8 = Label(root, text = hello)
    e.delete(0, 'end')
    myLabel8.pack(pady = 10)
    myButton['state'] = DISABLED

e = Entry(root, width = 50, font = ('Helvetica', 30))
e.pack(padx = 10, pady = 10)

myButton = Button(root, text = "Enter Your Name", command = myClick)
myButton.pack(pady = 10)

DeleteButton = Button(root, text = "Delete Text", command = myDelete)
DeleteButton.pack(pady = 10)

root.mainloop()