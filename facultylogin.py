from tkinter import*
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3
import re

def opennew():
    root.destroy()
    import facultreg

def datab():
    global conn,cursor
    conn=sqlite3.connect('facultymem.db')
    cursor=conn.cursor()

def circi():
    root.destroy()
    import circular
def reset():
    root.destroy()
    import facultforgot
    
def hide1():
    if var1.get()==1:
        entry2.configure(show="")
    elif var1.get()==0:
        entry2.configure(show="*")

def stulog():
    root.destroy()
    import project

def qiut():
    root.destroy()
    import project
#validating login
def validating_login():
    datab()
    if user_name.get()==""  or pass_word.get()=="":
        messagebox.showinfo("Information","Please fill all fields!")
    else:
        cursor.execute("SELECT username,password FROM Facult WHERE username=? and password=?",(user_name.get(),pass_word.get()))
        if cursor.fetchone() is not None:
            circi()
        else:
            messagebox.showinfo("Information","Invalid username or password")

#For designing
global root
root=Tk()
root.state('zoomed')

#design for tittle and logo
root.title("Welcome to Faculty Login")

#Background image
img2=Image.open('C:/Users/Abinaya/OneDrive/Desktop/Project/facultimg.jpg')
render=ImageTk.PhotoImage(img2)
img=Label(root,image=render)
img.place(x=0,y=0)

#frame for labels
frame=Frame(root,width=500,height=400,bg="White")
frame.pack(pady=160)
#Designing Label in the frame
form=Label(root,text="Faculty Login",width=20,font=("Californian FB",25),bg="White")
form.place(x=460,y=180)

#Designing username in the frame
user_name=StringVar()
pass_word=StringVar()
UserName=Label(root,text="User Name",width=20,font=("Californian FB",15),bg="White")
UserName.place(x=400,y=260)
entry1=Entry(root,textvariable=user_name,font=("Californian FB",15))
entry1.place(x=600,y=260)
img3=PhotoImage(file='C:/Users/Abinaya/OneDrive/Desktop/Project/icons8-user-male-30.png')
newimg3=Label(root,image=img3,bg="White")
newimg3.place(x=560,y=260)

#Designing password in the frame
password=Label(root,text="Password",width=20,font=("Californian FB",15),bg="White")
password.place(x=400,y=340)
entry2=Entry(root,show="*",textvariable=pass_word,font=("Californian FB",15))
entry2.place(x=600,y=340)
img4=PhotoImage(file='C:/Users/Abinaya/OneDrive/Desktop/Project/icons8-lock-26.png')
newimg4=Label(root,image=img4,bg="White")
newimg4.place(x=560,y=340)

#show password creation
var1=IntVar()
img5=PhotoImage(file='C:/Users/Abinaya/OneDrive/Desktop/Project/icons8-eye-24.png')
eyeimg5=Checkbutton(root,image=img5,command=hide1,offvalue=0,onvalue=1,variable=var1,relief=FLAT,bg="White")
eyeimg5.place(x=830,y=340)

#Designing login image
img6=PhotoImage(file='C:/Users/Abinaya/OneDrive/Desktop/Project/button.png')
loginimg6=Button(root,command=validating_login,image=img6,relief=FLAT,bg="White")
loginimg6.place(x=610,y=400)

#creating label for new user
cmt1=Label(root,text="If New User??",width=20,font=("Californian FB",15),bg="White")
cmt1.place(x=420,y=450)

#Designing create account
img7=PhotoImage(file='C:/Users/Abinaya/OneDrive/Desktop/Project/button (2).png')
createimg7=Button(root,image=img7,command=opennew,relief=FLAT,bg="white")
createimg7.place(x=610,y=450)

#dots
img10=PhotoImage(file='C:/Users/Abinaya/OneDrive/Desktop/Project/icons8-menu-vertical-24.png')
dotimg10=Menubutton(root,image=img10,relief=FLAT,bg="White")
dotimg10.menu=Menu(dotimg10)
dotimg10["menu"]=dotimg10.menu
dotimg10.menu.add_checkbutton(label="Student Login",font=("Californian FB",15),command=lambda:stulog())
dotimg10.menu.add_checkbutton(label="Quit",font=("Californian FB",15),command=lambda:qiut())
dotimg10.place(x=1200,y=10)

img61=PhotoImage(file='C:/Users/Abinaya/OneDrive/Desktop/Project/but3.png')
resetimg6=Button(root,command=reset,image=img61,relief=FLAT,bg="White")
resetimg6.place(x=580,y=490)
root.mainloop()
