from tkinter import*
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3

root=tk.Tk()
root.state('zoomed')
root.title("Login")
#design for tittle and logo
root.title("Welcome to Learnify")
imag=PhotoImage(file='C:/Users/Abinaya/OneDrive/Desktop/Project/new.png')
root.iconphoto(False,imag)

def on_close_window():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        exit(0)
        
def sub():
    root.destroy()
    import cls1subjects

def sub2():
    root.destroy()
    import cls2subjects

def connections():
    root.destroy()
    import connecting
    
def client():
    root.destroy()
    import clientgui

def study():
    root.destroy()
    import studyplan

def uploading():
    root.destroy()
    import browse
    
#Background image
img2=Image.open('C:/Users/Abinaya/OneDrive/Desktop/Project/1lik.jpg')
re=ImageTk.PhotoImage(img2)
img=Label(root,image=re)
img.place(x=0,y=0)

lab=Label(root,font=("Californian FB",15),bg="pink",height=300,width=6).pack(side="left")

img1=PhotoImage(file='C:/Users/Abinaya/OneDrive/Desktop/Project/icons8-home-50.png')
pn1=Button(root,image=img1,relief=FLAT,bg="pink")
pn1.place(x=5,y=100)
lab1=Label(root,text="Home",font=("Californian FB",15),bg="pink")
lab1.place(x=5,y=150)

img2=PhotoImage(file='C:/Users/Abinaya/OneDrive/Desktop/Project/icons8-relax-with-book-50.png')
pn2=Button(root,image=img2,command=study,relief=FLAT,bg="pink")
pn2.place(x=5,y=200)
plan=Label(root,text="Study\nPlan",font=("Californian FB",15),bg="pink")
plan.place(x=5,y=250)

img4=PhotoImage(file='C:/Users/Abinaya/OneDrive/Desktop/Project/icons8-information-50.png')
pn4=Button(root,image=img4,command=connections,relief=FLAT,bg="pink")
pn4.place(x=5,y=300)
circ=Label(root,text="Circu\nlars",font=("Californian FB",15),bg="pink")
circ.place(x=5,y=350)

img41=PhotoImage(file='C:/Users/Abinaya/OneDrive/Desktop/Project/icons8-upload-64.png')
pn41=Button(root,image=img41,command=uploading,relief=FLAT,bg="pink")
pn41.place(x=5,y=410)
circ1=Label(root,text="Upload",font=("Californian FB",15),bg="pink")
circ1.place(x=5,y=490)

img5=PhotoImage(file='C:/Users/Abinaya/OneDrive/Desktop/Project/icons8-messaging-50.png')
pn5=Button(root,image=img5,command=client,relief=FLAT,bg="pink")
pn5.place(x=5,y=520)
mess=Label(root,text="Messa\nges",font=("Californian FB",15),bg="pink")
mess.place(x=5,y=600)

back1=Button(root,text="Back",command=root.destroy,font=("Californian FB",15),bg="Snow",relief=FLAT)
back1.place(x=0,y=0)

mes=Label(root,text="Primary Classes",font=("Californian FB",50),bg="#071021",fg="white")
mes.place(x=400,y=10)

cls1=Button(root,text="Class 1",command=sub,width=20,height=2,font=("Californian FB",15),bg="snow",relief=FLAT)
cls1.place(x=500,y=100)

cls2=Button(root,text="Class 2",command=sub2,width=20,height=2,font=("Californian FB",15),bg="Snow",relief=FLAT)
cls2.place(x=500,y=200)

cls3=Button(root,text="Class 3",command=sub2,width=20,height=2,font=("Californian FB",15),bg="Snow",relief=FLAT)
cls3.place(x=500,y=300)

cls4=Button(root,text="Class 4",command=sub2,width=20,height=2,font=("Californian FB",15),bg="Snow",relief=FLAT)
cls4.place(x=500,y=400)

cls5=Button(root,text="Class 5",command=sub2,width=20,height=2,font=("Californian FB",15),bg="Snow",relief=FLAT)
cls5.place(x=500,y=500)

imge2=PhotoImage(file='C:/Users/Abinaya/OneDrive/Desktop/Project/icons8-logout-rounded-left-50.png')
pne2=Button(root,image=imge2,command=on_close_window,relief=FLAT,bg="white")
pne2.place(x=1200,y=0)
plane=Label(root,text="LogOut",font=("Californian FB",15),bg="White")
plane.place(x=1200,y=55)

root.mainloop()


