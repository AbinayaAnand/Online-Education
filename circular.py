from tkinter import*
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3
import datetime

root=Tk()
root.state('zoomed')
img21=Image.open('C:/Users/Abinaya/OneDrive/Desktop/Project/1lik.jpg')
render1=ImageTk.PhotoImage(img21)
img21=Label(root,image=render1)
img21.place(x=0,y=0)

def bakc1():
        root.destroy()
        import project

def client():
    root.destroy()
    import clientfac
    
#design for tittle and logo
root.title("Welcome to The Students Login")
circular=StringVar()
def studcircu():
        cir=circular.get()
        now=datetime.datetime.now()
        datt=(now.strftime("%d-%m-%y - %H:%M:%S"))
        if cir=="":
            messagebox.showinfo("Information","Fill Required Fields")
        else:            
            conn=sqlite3.connect('circula1.db')
            with conn:
                cursor=conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS Cirucularstudents (Circular TEXT,Datetime TEXT)')
            cursor.execute('INSERT INTO Cirucularstudents(Circular,Datetime) VALUES(?,?)',(cir,datt))
            print("Database successfully Opened")
            conn.commit()
            messagebox.showinfo("Information","Successfully uploaded")


circu=Label(root,text="Circular Session",width=20,font=("Californian FB",35),fg="white",bg="#071021")
circu.place(x=380,y=60)
entry1=Entry(root,width=40,textvariable=circular,font=("Californian FB",15))
entry1.place(x=450,y=200)

bakc=Button(root,text="back",command=bakc1,font=("Californian FB",15),bg="White",relief=FLAT)
bakc.place(x=0,y=0)

img5=PhotoImage(file='C:/Users/Abinaya/OneDrive/Desktop/Project/icons8-messaging-50.png')
pn5=Button(root,image=img5,command=client,relief=FLAT,bg="pink")
pn5.place(x=5,y=520)
mess=Label(root,text="Messa\nges",font=("Californian FB",15),bg="pink")
mess.place(x=5,y=600)

butto=Button(root,text="Submit",command=studcircu,width=20,font=("Californian FB",15),bg="White",relief=FLAT)
butto.place(x=530,y=490)



root.mainloop()

