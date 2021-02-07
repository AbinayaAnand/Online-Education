from tkinter import*
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3


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

def engcls2():
    root.destroy()
    import cls2english
    
def hindicls2():
    root.destroy()
    import cls2hindi

def evscls2():
    root.destroy()
    import cls2evs

def gkcls2():
    root.destroy()
    import cls2gk

def mathcls2():
    root.destroy()
    import cls2math
back2=Button(root,text="Back",command=bbk,font=("Californian FB",15),bg="white",relief=FLAT)
back2.place(x=0,y=0)

cllsen=Button(root,text="English",command=engcls2,width=20,height=2,font=("Californian FB",15),bg="white",relief=FLAT)
cllsen.place(x=500,y=100)

cllshi=Button(root,text="Hindi",command=hindicls2,width=20,height=2,font=("Californian FB",15),bg="white",relief=FLAT)
cllshi.place(x=500,y=200)

cllsma=Button(root,text="Maths",command=mathcls2,width=20,height=2,font=("Californian FB",15),bg="white",relief=FLAT)
cllsma.place(x=500,y=300)

cllsgk=Button(root,text="GK",command=gkcls2,width=20,height=2,font=("Californian FB",15),bg="white",relief=FLAT)
cllsgk.place(x=500,y=400)

cllsevs=Button(root,text="EVS",command=evscls2,width=20,height=2,font=("Californian FB",15),bg="white",relief=FLAT)
cllsevs.place(x=500,y=500)

root.mainloop()
