from tkinter import*
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3
import re

def subjects():
    root.destroy()
    import firstpage

def database():
    global conn,cursor
    conn=sqlite3.connect('datab.db')
    cursor=conn.cursor()#fetch data

def hide():
    if var.get()==1:
        entry2.configure(show="")
    elif var.get()==0:
        entry2.configure(show="*")

def reset():
    root.destroy()
    import email
#validating login
def validating_login():
    database()
    if user_name.get()==""  or pass_word.get()=="":
        messagebox.showinfo("Information","Please fill all fields!")
    else:
        cursor.execute("SELECT username,password FROM Candidate WHERE username=? and password=?",(user_name.get(),pass_word.get()))
        if cursor.fetchone() is not None:
            subjects()
        else:
            messagebox.showinfo("Information","Invalid username or password")

def opennew():
    root.destroy()
    import registration

def faculty():
    root.destroy()
    import facultylogin
    
#For designing
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
frame=Frame(root,width=500,height=400,bg="White")
frame.pack(pady=160)
#Designing Label in the frame
form=Label(root,text="Student Login",width=20,font=("Californian FB",25),bg="White")
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
var=IntVar()
img5=PhotoImage(file='C:/Users/Abinaya/OneDrive/Desktop/Project/icons8-eye-24.png')
eyeimg5=Checkbutton(root,image=img5,command=hide,offvalue=0,onvalue=1,variable=var,relief=FLAT,bg="White")
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

#Design for teacher button
img9=PhotoImage(file='C:/Users/Abinaya/OneDrive/Desktop/Project/button (3).png')
facultyimg9=Button(root,image=img9,command=faculty,relief=FLAT,bg="#9e7768")
facultyimg9.place(x=1100,y=40)

#dots
imga10=PhotoImage(file='C:/Users/Abinaya/OneDrive/Desktop/Project/icons8-menu-vertical-24.png')
dottimg10=Menubutton(root,image=imga10,relief=FLAT,bg="White")
dottimg10.menu=Menu(dottimg10)
dottimg10["menu"]=dottimg10.menu
dottimg10.menu.add_checkbutton(label="Faculty Login",font=("Californian FB",15),command=lambda:faculty())
dottimg10.menu.add_checkbutton(label="Quit",font=("Californian FB",15),command=lambda:root.destroy())
dottimg10.place(x=1200,y=40)

img61=PhotoImage(file='C:/Users/Abinaya/OneDrive/Desktop/Project/but3.png')
resetimg6=Button(root,command=reset,image=img61,relief=FLAT,bg="White")
resetimg6.place(x=580,y=490)

root.mainloop()





