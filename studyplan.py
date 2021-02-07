from tkinter import*
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox

root=tk.Tk()
root.state('zoomed')
root.title("Study Plan")

img12=Image.open('C:/Users/Abinaya/OneDrive/Desktop/Project/1lik.jpg')
re1=ImageTk.PhotoImage(img12)
img11=Label(root,image=re1)
img11.place(x=0,y=0)

imgcs=Image.open('C:/Users/Abinaya/OneDrive/Desktop/Project/ssf.png')
rimcs=ImageTk.PhotoImage(imgcs)
imgcs=Label(root,image=rimcs)
imgcs.place(x=100,y=100)

def funct():
    root.destroy()
    import firstpage

backkk=Button(root,text="Back",command=funct,font=("Californian FB",15),bg="Snow",relief=FLAT)
backkk.place(x=0,y=0)
