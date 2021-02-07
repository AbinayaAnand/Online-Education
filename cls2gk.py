from tkinter import*
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox

root=tk.Tk()
root.state('zoomed')
root.title("std1")
root.configure(background="white")

def fn3():
    root.destroy()
    import cls2subjects

back1=Button(root,text="Back",command=fn3,font=("Californian FB",15),bg="Snow",relief=FLAT)
back1.place(x=0,y=0)

imgccs=Image.open('C:/Users/Abinaya/OneDrive/Desktop/Project/Screenshot (130).png')
rimccs=ImageTk.PhotoImage(imgccs)
imgccs=Label(root,image=rimccs)
imgccs.pack(anchor='center')
