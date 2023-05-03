from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
import re

class loginPage:
    def __init__(self,root):

        self.root=root
        self.root.title("Login Page")
        self.root.state("zoomed")
        
        #variables
        self.id=StringVar()
        self.password=StringVar()

        # Image
        self.bg=ImageTk.PhotoImage(file="photo1.jpg")
        bgLbl=Label(self.root,image=self.bg,relief=RAISED)
        bgLbl.place(height=900,width=1600,x=0,y=0)

        # hadder frame  
        hadder_frame = Frame(self.root, bd=1, relief=RIDGE,background="gray")
        hadder_frame.place(x=500, y=200, width=550, height=70)

        hadder_name = Label(hadder_frame, text="Login",bg="gray", font=("times new roman", 28, "bold"))
        hadder_name.grid(row=0, column=0, padx=220, pady=10, sticky=W)

        # main frame
        main_frame = Frame(self.root, bd=1, relief=RIDGE,background="white")
        main_frame.place(x=500, y=270, width=550, height=300)

        # Login id
        Login_id = Label(main_frame, text="Username:", font=("times new roman", 18, "bold"))
        Login_id.grid(row=0, column=0, padx=30, pady=20, sticky=W)

        self.Login_id_Entry = ttk.Entry(main_frame, font=("arial", 18),textvariable=self.id, width=22)
        self.Login_id_Entry.grid(row=0, column=1, padx=5, pady=20, sticky=W)

        # Password
        Password = Label(main_frame, text="Password :", font=("times new roman", 18, "bold"))
        Password.grid(row=1, column=0, padx=30, pady=20, sticky=W)

        self.Password_Entry = ttk.Entry(main_frame, font=("arial", 18),textvariable=self.password,show="*", width=22)
        self.Password_Entry.grid(row=1, column=1, padx=5, pady=20, sticky=W)

        #login
        
        login_button=Button(main_frame,text="LOGIN",font=("arial",15,"bold"),bd=5,width=15,cursor="hand2",bg="sky blue",activebackground="gray",command=self.connection)
        login_button.place(x=270,y=200,height=50,width=150)

   #    Back
        back=Button(main_frame,text="Back",font=("arial",15,"bold"),bd=5,width=15,cursor="hand2",bg="sky blue",activebackground="gray",command=self.back_fun)
        back.place(x=90,y=200,height=50,width=150)
    
       

    def connection(self):
        
        self.username = self.Login_id_Entry.get()
        password = self.Password_Entry.get()
                
        conn=pymysql.connect(host="localhost",user="root",password="root",database="db_quiz")
        cur=conn.cursor() 

        cur.execute("SELECT password FROM Registration_tb WHERE username=%s", (self.username,))
        result = cur.fetchone()
       # print(result)
        
        # Check if the entered password matches the one in the database
        if result and result[0] == password:
          
            messagebox.showinfo("login","Login sucessfully") 
            from Admin import display
            a=display(self.root,self.id.get()) 
        else:
            #message_label.config(text="Incorrect username or password.")
            messagebox.showerror("login","Login id or Password incorrect")  

    def back_fun(self):        
        from main_page import display
        a=display(self.root)
           
def second():
    root=Tk()
    obj=loginPage(root=root)
    root.mainloop()
    
if __name__=="__main__":
    second()