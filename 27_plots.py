from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title('Tu nerd')
root.geometry("400x200")

def graph():
    housePrices = np.random.normal(200000, 25000, 5000)
    #plt.hist(housePrices, 200)
    plt.polar(housePrices)
    plt.show()

myButton = Button(root, text = "Graph It!", command = graph)
myButton.pack()

root.mainloop()