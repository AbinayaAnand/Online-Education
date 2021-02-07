from tkinter import *
from tkinter import ttk #tk themed widget
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3

def data1():
    global conn,cursor
    conn=sqlite3.connect('circula1.db')
    cursor=conn.cursor()

def rewind():
    root.destroy()
    import firstpage
    
#validating login
def showing():
    data1()
    cursor.execute("SELECT * FROM Cirucularstudents")
    r=cursor.fetchall()
    for i in r:
        tree.insert("",tk.END,values=i,tags='T')
        tree.tag_configure('T',font=("Arial",15))
    conn.close()

root=tk.Tk()
frame1=Frame(root,width=5000,height=8000,bd=50)
frame1.pack()

style=ttk.Style()
style.configure("Treeview",background="Silver",rowheight=25,fieldbackgroung="Silver")
tree=ttk.Treeview(frame1,columns=("#1","#2"),show='headings')
tree.heading("#1",text="Circular")
tree.heading("#2",text="Date & Time")
tree.column("#1",minwidth=0,width=500,stretch=NO)
tree.column("#2",minwidth=0,width=500,stretch=NO)
tree.pack(fill='x')#filling the entire space 
tree.place(x=100,y=100)

            
back9=Button(text="Back",command=rewind,font=("Californian FB",15),bg="pink",relief=FLAT)
back9.place(x=0,y=0)

showing()
#design for tittle and logo
root.state('zoomed')
root.title("Welcome to The notification")
root.mainloop()
