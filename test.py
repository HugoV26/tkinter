from tkinter import *

def showAbout(self):


       if self.aboutOpen==0:
           self.about=Tk()
           self.about.title("About "+ self.programName)

           Label(self.about,text="%s: Version 1.0" % self.programName ,foreground='blue').pack()
           Label(self.about,text="By Vidar").pack()
           self.contact=Label(self.about,text="Contact: adress@gmail.com",font=("Helvetica", 10))
           self.contact.pack()
           self.closeButton=Button(self.about, text="Close", command = lambda: self.showAbout())
           self.closeButton.pack()
           self.about.geometry("%dx%d+%d+%d" % (175,\
                                           95,\
                                           self.myParent.winfo_rootx()+self.myParent.winfo_width()/2-75,\
                                           self.myParent.winfo_rooty()+self.myParent.winfo_height()/2-35))

           self.about.resizable(0,0)
           self.aboutOpen=1
           self.about.protocol("WM_DELETE_WINDOW", lambda: self.showAbout())
           self.closeButton.focus_force()


           self.contact.bind('<Leave>', self.contactMouseOver)
           self.contact.bind('<Enter>', self.contactMouseOver)
           self.contact.bind('<Button-1>', self.mailAuthor)
       else:
           self.about.destroy()
           self.aboutOpen=0

def contactMouseOver(self,event):

       if event.type==str(7):
           self.contact.config(font=("Helvetica", 10, 'underline'))
       elif event.type==str(8):
           self.contact.config(font=("Helvetica", 10))

def mailAuthor(self,event):
       import webbrowser
       webbrowser.open('mailto:adress@gmail.com',new=1)