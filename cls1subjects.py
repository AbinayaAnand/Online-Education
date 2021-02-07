from tkinter import*
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3
import re
import os
import mysql.connector

root=tk.Tk()
root.state('zoomed')
root.title("std1")
img2=Image.open('C:/Users/Abinaya/OneDrive/Desktop/Project/1lik.jpg')
re=ImageTk.PhotoImage(img2)
img=Label(root,image=re)
img.place(x=0,y=0)

def bbk():
   root.destroy() 
   import firstpage
   
def engcls1():
    root.destroy()
    import cls1english
    
def hindicls1():
    root.destroy()
    import cls1hindi

def evscls1():
    root.destroy()
    import cls1evs

def gkcls1():
    root.destroy()
    import cls1gk

def mathcls1():
    root.destroy()
    import cls1math

back2=Button(root,text="Back",command=bbk,font=("Californian FB",15),bg="white",relief=FLAT)
back2.place(x=0,y=0)

cllsen=Button(root,text="English",command=engcls1,width=20,height=2,font=("Californian FB",15),bg="white",relief=FLAT)
cllsen.place(x=500,y=100)

cllshi=Button(root,text="Hindi",command=hindicls1,width=20,height=2,font=("Californian FB",15),bg="white",relief=FLAT)
cllshi.place(x=500,y=200)

cllsma=Button(root,text="Maths",command=mathcls1,width=20,height=2,font=("Californian FB",15),bg="white",relief=FLAT)
cllsma.place(x=500,y=300)

cllsgk=Button(root,text="GK",command=gkcls1,width=20,height=2,font=("Californian FB",15),bg="white",relief=FLAT)
cllsgk.place(x=500,y=400)

cllsevs=Button(root,text="EVS",command=evscls1,width=20,height=2,font=("Californian FB",15),bg="white",relief=FLAT)
cllsevs.place(x=500,y=500)

if __name__=="__main__":
   root.mainloop()
