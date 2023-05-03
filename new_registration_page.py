from tkinter import *
from  tkinter import ttk
from PIL import Image,ImageTk
import pymysql
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter import messagebox

class new_registration:
    def __init__(self,root):
        self.root=root
        self.root.title("New registration")
        self.root.state("zoomed")

        # variables
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.gender_var.set("no")
        self.categ_var = StringVar()
        self.password_var = StringVar()
        self.confirm_var = StringVar()
        self.Img_var=Variable()
        
        

        #Image
        self.bg=ImageTk.PhotoImage(file="photo1.jpg")
        bgLbl=Label(self.root,image=self.bg,relief=RAISED)
        bgLbl.place(height=900,width=1600,x=0,y=0)
         
        #hadder Frame
        hadder_frame = Frame(self.root, bd=1, relief=RIDGE,bg="gray")
        hadder_frame.place(x=500, y=90, width=550, height=70)

        hadder_name = Label(hadder_frame, text="New registration", font=("times new roman",28, "bold"),bg="gray")
        hadder_name.grid(row=0, column=0, padx=150, pady=10, sticky=W)

        #main frame
        main_frame = Frame(self.root, bd=1, relief=RIDGE)
        main_frame.place(x=500, y=160, width=550, height=500)

        # Username
        user_name = Label(main_frame, text="Username:", font=("times new roman", 16, "bold"))
        user_name.grid(row=0, column=0, padx=30, pady=10, sticky=W)
        user_Entry = ttk.Entry(main_frame,textvariable=self.name_var, font=("arial", 15), width=22)
        user_Entry.grid(row=0, column=1, padx=5, pady=10, sticky=W)

        # Email
        user_email = Label(main_frame, text="Email Id:", font=("times new roman", 16, "bold"))
        user_email.grid(row=1, column=0, padx=30, pady=10, sticky=W)
        email_Entry = ttk.Entry(main_frame,textvariable=self.email_var, font=("arial", 15), width=22)
        email_Entry.grid(row=1, column=1, padx=5, pady=10, sticky=W)

        # Gender frame
        user_Gender = Label(main_frame, text="Gender:", font=("times new roman", 16, "bold"))
        user_Gender.grid(row=3, column=0, padx=30, pady=10, sticky=W)

        # Gender 
        gen_Frame = Frame(main_frame)
        gen_Frame.place(x=229, y=110, width=280, height=35)
        rdoM = Radiobutton(gen_Frame,variable=self.gender_var, value="Male", text="Male",
                           font=("times new roman", 15))  # variable=self.gender.var
        rdoM.grid(row=0, column=0, padx=10, pady=0, sticky=W)
      
        rdoF = Radiobutton(gen_Frame, variable=self.gender_var, value="Female", text="Female",
                           font=("times new roman", 15))
        rdoF.grid(row=0, column=1, padx=10, pady=0, sticky=W)

        #create password
        create_password = Label(main_frame, text="Create password :", font=("times new roman", 16, "bold"))
        create_password.grid(row=5, column=0, padx=30, pady=10, sticky=W)
        create_password_Entry = ttk.Entry(main_frame,textvariable=self.password_var, font=("arial", 15), width=22,show="*")
        create_password_Entry.grid(row=5, column=1, padx=5, pady=10, sticky=W)

        # re-enter password
        re_enter_password = Label(main_frame, text="Confirm password :", font=("times new roman", 16, "bold"))
        re_enter_password.grid(row=6, column=0, padx=30, pady=10, sticky=W)
        re_enter_password_Entry = ttk.Entry(main_frame,textvariable=self.confirm_var, font=("arial", 15), width=22,show="*")
        re_enter_password_Entry.grid(row=6, column=1, padx=5, pady=10, sticky=W)

        #Upload image
        uploadL = Label(main_frame,font=("times new roman", 16, "bold"))  
        uploadL.grid(row=7,column=0, padx=30, pady=10, sticky=W)        
        UpldBtn = Button(main_frame, text='Upload Image',width=22,command = lambda:self.upload_file())
        UpldBtn.grid(row=7,column=1, padx=5, pady=10, sticky=W)




        #submit
        submit=Button(main_frame,text="SUBMIT",font=("arial",15,"bold"),width=15,cursor="hand2",bg="light blue",bd="5",activebackground="gray",command=self.connection)
        submit.place(x=100,y=400,height=40,width=140)

        bk_btn=Button(main_frame,text="BACK",font=("arial",15,"bold"),width=15,cursor="hand2",bg="light blue",bd="5",activebackground="gray",command=self.back_fun)
        bk_btn.place(x=300,y=400,height=40,width=140)


        self.main=main_frame

    def upload_file(self):
        
        f_types = [('Jpg Files', '*.jpg'),('PNG Files','*.png')]                # type of files to select 
        filename =filedialog.askopenfilename(multiple=True,filetypes=f_types)
        
        for f in filename:
            img=Image.open(f)               # read the image file
         
            img=img.resize((80,80))         # new width & height            
            img=ImageTk.PhotoImage(img)
            
            e1 =Label(self.main,text="img")
            e1.grid(row=7,column=0)
            e1.image = img                  # keep a reference! by attaching it to a widget attribute
            e1['image']=img                 # Show Image  
            
            self.Img_var=img
    def back_fun(self):
        from main_page import display
        a=display(self.root)




    def connection(self):
        if  self.name_var.get()=="" or self.email_var.get()=="" or self.gender_var.get()=="" :
            messagebox.showwarning("Warning","Plese enter all fields")

        else:
            conn=pymysql.connect(host="localhost",user="root",password="root",database="db_quiz")
            cur=conn.cursor()  
            cur.execute("Insert into registration_tb (USERNAME,EMAIL,GENDER,PASSWORD,RECHACK_PASS) values(%s,%s,%s,%s,%s)",({self.name_var.get()},{self.email_var.get()},{self.gender_var.get()},{self.password_var.get()},{self.confirm_var.get()})) 
            messagebox.showinfo("Register","Successfully Register")
            from login_page import loginPage
            a=loginPage(self.root,)
            conn.commit()
        
        
def new_reg():
    root = Tk()
    obj = new_registration(root=root)
 
    root.mainloop()

if __name__=="__main__":
    new_reg()