from tkinter import * 

root = Tk()
root.title("Insert method")

e1 = Entry(root, width = 35)
e1.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
e1.insert(0, "hello")
e1.insert("end", "world")
e1.insert(5, ", ")

root.mainloop()