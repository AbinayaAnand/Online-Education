from tkinter import*
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox

root=tk.Tk()
root.state('zoomed')
root.title("std1")
root.configure(background="white")

def fn2():
    root.destroy()
    import cls1subjects

back1=Button(root,text="Back",command=fn2,font=("Californian FB",15),bg="Snow",relief=FLAT)
back1.place(x=0,y=0)

imgcs=Image.open('C:/Users/Abinaya/OneDrive/Desktop/Project/Screenshot (126).png')
rimcs=ImageTk.PhotoImage(imgcs)
imgcs=Label(root,image=rimcs)
imgcs.pack(anchor='center')

img4cs=PhotoImage(file='C:/Users/Abinaya/OneDrive/Desktop/Project/button (1).png')
newimg4cs=Label(root,image=img4cs,bg="White")
newimg4cs.place(x=500,y=0)

