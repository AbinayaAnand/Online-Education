from tkinter import*
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3
import re

def database():
    global conn,cursor
    conn=sqlite3.connect('facultymem.db')
    cursor=conn.cursor()#fetch data

def new():
    root.destroy()
    import project
def collecting():
    if newpass_word.get()==""  or conpass_word.get()=="":
        messagebox.showinfo("Information","Please fill all fields!")
    else:
        checking()
def checking():
    if newpass_word.get()!=conpass_word.get():
                messagebox.showinfo("Information","password mismatch")
    else:
        database()
        cursor.execute("SELECT emailid FROM Facult WHERE username=?",[user_name.get()])
        if cursor.fetchone() is not None:
            database()
            cursor.execute("UPDATE Facult SET password=? WHERE username=?",([newpass_word.get(),user_name.get()]))
            conn.commit()
            new()
        else:
             messagebox.showinfo("Information","UserName Not Found")

root=Tk()#creates a main window called root
root.state('zoomed')

#design for tittle and logo
root.title("Welcome to The Students Login")

#Background image
img2=Image.open('C:/Users/Abinaya/OneDrive/Desktop/Project/resize.jpg')
rim=ImageTk.PhotoImage(img2)
img=Label(root,image=rim)
img.place(x=0,y=0)

#frame for labels
frame=Frame(root,width=500,height=600,bg="White")
frame.pack(pady=160)

formm=Label(root,text="Forgot Password",width=20,font=("Californian FB",25),bg="White")
formm.place(x=460,y=180)

newpass_word=StringVar()
conpass_word=StringVar()
user_name=StringVar()

newpassword=Label(root,text="New Password",width=20,font=("Californian FB",15),bg="White")
newpassword.place(x=400,y=260)
entry2=Entry(root,textvariable=newpass_word,font=("Californian FB",15))
entry2.place(x=600,y=260)

conpassword=Label(root,text="Confirm Password",width=20,font=("Californian FB",15),bg="White")
conpassword.place(x=400,y=340)
entry2=Entry(root,textvariable=conpass_word,font=("Californian FB",15))
entry2.place(x=600,y=340)

passemail=Label(root,text="UserName",width=20,font=("Californian FB",15),bg="White")
passemail.place(x=400,y=420)
entryemail=Entry(root,textvariable=user_name,font=("Californian FB",15))
entryemail.place(x=600,y=420)
img9=PhotoImage(file='C:/Users/Abinaya/OneDrive/Desktop/Project/butooooo.png')
resetimg9=Button(root,image=img9,command=collecting,relief=FLAT)
resetimg9.place(x=610,y=470)
