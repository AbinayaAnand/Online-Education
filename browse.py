from tkinter import*
import tkinter as tk
from tkinter import filedialog
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3
import re
import os

class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.img2=Image.open('C:/Users/Abinaya/OneDrive/Desktop/Project/1lik.jpg')
        self.re=ImageTk.PhotoImage(self.img2)
        self.img=Label(self,image=self.re)
        self.img.place(x=0,y=0)
        self.openn=tk.Label(self,text="Select a File",width=20,font=("Californian FB",15),bg="White")
        self.openn.place(x=400,y=200,height=100,width=500)
        self.button()

    def button(self):
        self.browse=tk.Button(self,command=self.fileDialog,width=20,text="Browse A File",font=("Californian FB",15),relief=FLAT,bg="Deep Pink")
        self.browse.place(x=400,y=300,height=100,width=500)
        self.back1=tk.Button(self,text="Back",command=self.bc,font=("Californian FB",15),bg="Snow",relief=FLAT)
        self.back1.place(x=0,y=0)
        self.upload=tk.Button(self,width=20,text="Upload",command=self.upload,font=("Californian FB",15),relief=FLAT,bg="white")
        self.upload.place(x=550,y=500)

    def fileDialog(self):
        self.filename=filedialog.askopenfile()
        self.labell=tk.Label(text=self.filename,font=("Californian FB",15),bg="White")
        self.labell.place(x=300,y=600)

    def upload(self):
        messagebox.showinfo("Information","Updated succesfully")
        root.destroy()
        import firstpage
    def bc(self):
        self.destroy()
        import firstpage

#creates a main window called root
root=Root()
root.state('zoomed')
root.mainloop()


