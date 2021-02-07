from tkinter import*
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3
import re
import os
import mysql.connector

class Project:
    def __init__(self,window):
        window.title("Welcome to Learnify")
        window.state('zoomed')
        self.imgg=Image.open('C:/Users/Abinaya/OneDrive/Desktop/Project/facultimg.jpg')
        self.im=ImageTk.PhotoImage(self.imgg)
        self.img=Label(window,image=self.im)
        self.img.place(x=0,y=0)
        self.frame=Frame(window,width=800,height=1000,bg="White")
        self.frame.pack(pady=50)

        self.form=Label(window,text="Faculty Registration",width=20,font=("Algerian",20),bg="White")
        self.form.place(x=430,y=60)
        
        self.use_name=StringVar()
        self.val_id=StringVar()
        self.email_id=StringVar()
        self.phone_num=StringVar()
        self.pass_word=StringVar()
        self.confirm_password=StringVar()
        self.val_address=StringVar()
        self.val_gender=IntVar()
        self.val_dob=StringVar()
        self.val_username=StringVar()
        self.val_password=StringVar()

        self.username=Label(window,text="First Name",width=20,font=("bold",10),bg="white")
        self.username.place(x=250,y=130)
        self.entry1=Entry(window,textvariable=self.use_name,font=("bold",10))
        self.entry1.place(x=400,y=130)

        self.val_idd=Label(window,text="Faculty Id",width=20,font=("bold",10),bg="white")
        self.val_idd.place(x=250,y=200)
        self.ent2=Entry(window,textvariable=self.val_id,font=("bold",10))
        self.ent2.place(x=400,y=200)
        
        self.emailid=Label(window,text="Email Id",width=20,font=("bold",10),bg="white")
        self.emailid.place(x=600,y=200)
        self.entry3=Entry(window,textvariable=self.email_id,font=("bold",10))
        self.entry3.place(x=750,y=200)

        self.phnum=Label(window,text="Phone Number",width=20,font=("bold",10),bg="white")
        self.phnum.place(x=250,y=270)
        self.entry4=Entry(window,textvariable=self.phone_num,font=("bold",10))
        self.entry4.place(x=400,y=270)

        self.password=Label(window,text="Password",width=20,font=("bold",10),bg="white")
        self.password.place(x=600,y=270)
        self.entry5=Entry(window,show="*",textvariable=self.pass_word,font=("bold",10))
        self.entry5.place(x=750,y=270)

        self.confirm=Label(window,text="Confirm Password",width=20,font=("bold",10),bg="white")
        self.confirm.place(x=250,y=340)
        self.entry6=Entry(window,show="*",textvariable=self.confirm_password,font=("bold",10))
        self.entry6.place(x=400,y=340)

        self.address=Label(window,text="Residential Address",width=20,font=("bold",10),bg="white")
        self.address.place(x=600,y=340)
        self.entry7=Entry(window,textvariable=self.val_address,font=("bold",10))
        self.entry7.place(x=750,y=340)

        self.gender=Label(window,text="Gender",width=20,font=("bold",10),bg="white")
        self.gender.place(x=600,y=420)
        self.but=Radiobutton(window,text="Male",padx=5,variable=self.val_gender,value=1,bg="white").place(x=750,y=420)
        self.but=Radiobutton(window,text="Female",padx=20,variable=self.val_gender,value=2,bg="white").place(x=800,y=420)

        self.dob=Label(window,text="DOB",width=20,font=("bold",10),bg="white")
        self.dob.place(x=280,y=420)
        self.entry8=Entry(window,textvariable=self.val_dob,font=("bold",10))
        self.entry8.place(x=400,y=420)

        self.user=Label(window,text="Already Existing user?",width=20,font=("bold",10),bg="white").place(x=500,y=600)

        self.backy=Button(window,text="Back",command=self.callin,font=("Californian FB",15),bg="Snow",relief=FLAT)
        self.backy.place(x=0,y=0)

        self.register=Button(window,text="REGISTER",command=self.validating,bg="Cyan",font=("bold",10)).place(x=450,y=500)
        self.clear=Button(window,text="CLEAR",command=self.clearreset,bg="Cyan",font=("bold",10)).place(x=650,y=500)
        self.exiit=Button(window,text="EXIT",command=self.callnewscreen,bg="Cyan",font=("bold",10)).place(x=850,y=500)
        self.login=Button(window,text="LOGIN",command=self.loginscreen,bg="Cyan",font=("bold",10)).place(x=650,y=600)
    def validate_username(self,username):
        if username.isalpha():
            return True
        elif username=="":
            return True
        else:
            messagebox.showinfo('Information','Only characters are allowed')
            return False

    def validate_email(self,emailid):
        if len(emailid)>7:
            if re.match("^[a-zA-Z0-9]+[@]+[a-zA-Z0-9].[a-z]",emailid)!=None:
                return True
            return False
        else:
            messagebox.showinfo("Information","Not a valid email check again")
            return False
    
    def validate_password(self,password):
        if len(password)>8:
            if re.match("a-zA-z0-9!@#$%^&*?.><",password):
                return True
            return False
        else:
            messagebox.showinfo("Information","Invalid password it should have atleast one upper lower and specialcharacters and should be greater than ")
            return False

    def validate_confirmpassword(self,confirmpassword):
        if len(confirmpassword)>8:
            if re.match("a-zA-z0-9!@#$%^&*?.><",confirmpassword):
                return True
            return False
        else:
            messagebox.showinfo("Information","Invalid password it should have atleast one upper lower and specialcharacters")
            return False
    
    def validating(self):
        if self.use_name.get()=="":
            messagebox.showinfo("Information","User Name is mandatory")
        elif self.use_name.get()!="":
            status1=self.validate_username(self.use_name.get())
            
        if self.val_id.get()=="":
            messagebox.showinfo("Information","Id is mandatory")
        elif self.val_id.get()!="":
            pass
        
        if self.email_id.get()=="":
            messagebox.showinfo("Information","Email Id is mandatory")
        elif self.email_id.get()!="":
            status3=self.validate_email(self.email_id.get())
        
        if self.phone_num.get()=="":
            messagebox.showinfo("Information","Phone Number is mandatory")
        elif len(self.phone_num.get())!=10:
            messagebox.showinfo("Information","Enter 10 digit phone number")
            
        if self.pass_word.get()=="":
            messagebox.showinfo("Information","Password is mandatory")
        elif self.pass_word.get()!="":
            status4=self.validate_password(self.pass_word.get())
            
        if self.confirm_password.get()=="":
            messagebox.showinfo("Information","Confirm Password is mandatory")
        elif self.confirm_password.get()!="":
            status5=self.validate_confirmpassword(self.confirm_password.get())
            
        if self.pass_word.get()!=self.confirm_password.get():
            messagebox.showinfo("Information","password mismatch")

        elif self.val_address.get()=="":
            messagebox.showinfo("Information","address is mandatory")
            
        elif self.val_gender.get()==0:
            messagebox.showinfo("Information","Gender is mandatory")
            
        elif self.val_dob.get()=="":
            messagebox.showinfo("Information","DOB is mandatory") 

        elif self.val_id.get()=="":
            messagebox.showinfo("Information","Faculty Id is mandatory") 
        
        else:
            messagebox.showinfo("Information","successfully registered")
            val=self.database()
        
    
    def database(self):
        UserName=self.use_name.get()
        Id=self.val_id.get()
        Mail=self.email_id.get()
        Phone=self.phone_num.get()
        Password=self.pass_word.get()
        Addre=self.val_address.get()
        Gend=self.val_gender.get()
        Doob=self.val_dob.get()
        conn=sqlite3.connect('facultymem.db')
        with conn:
            cursor=conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Facult(UserName TEXT,FacultyId TEXT,EmailId TEXT,PhoneNum TEXT,PassWord TEXT,Address TEXT,Gender TEXT,DOB TEXT)')
        cursor.execute('INSERT INTO Facult(UserName,FacultyId,EmailId,PhoneNum,PassWord,Address,Gender,DOB) VALUES(?,?,?,?,?,?,?,?)',(UserName,Id,Mail,Phone,Password,Addre,Gend,Doob,))
        print("Database successfully Opened")
        conn.commit()
        messagebox.showinfo("Information","Login the username and password")
        
    def clearreset(self):
        self.use_name.set("")
        self.val_id.set("")
        self.email_id.set("")
        self.phone_num.set("")
        self.pass_word.set("")
        self.confirm_password.set("")
        self.val_address.set("")
        self.val_gender.set("")
        self.val_dob.set("")

    def callnewscreen(self):
        window.destroy()
        import facultylogin

    def loginscreen(self):
        window.destroy()
        import facultylogin

    def callin(self):
        window.withdraw()
        
global window    
window=Tk()
obj=Project(window)
window.mainloop()
   

