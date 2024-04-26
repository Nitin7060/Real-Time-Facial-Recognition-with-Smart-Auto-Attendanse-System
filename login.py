from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk           # pip install Pillow
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from main import Face_Recognition_System


def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()


class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        #self.bg=ImageTk.PhotoImage(file=r"C:\Users\Nitin\Desktop\Login form\college_images\college_images\hackers2.jpg")
        #lbl_bg=Label(self.root,image=self.bg)
        #lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        #frame=Frame(self.root,bg="black")
        #frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\Nitin\Desktop\Login form\college_images\college_images\LoginIconAppl.png")
        img1=img1.resize((1530,750),Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        bg_lbl=Label(self.root,image=self.photoimage1)
        bg_lbl.place(x=0,y=0,width=1530,height=750)

        title=Label(bg_lbl,text="FACIAL RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20,"bold"),fg="white",bg="black")
        title.place(x=0,y=120,width=1550,height=45)

        

        # project button ==============================
        downtitle=Label(self.root,text="Note:Enter valid username and valid password",font=("times new roman",20,"bold"),fg="white",bg="black")
        downtitle.place(x=0,y=740,width=1600,height=35)

        img10 = Image.open(r"C:\Users\Nitin\Desktop\facial recognition system\college_images\college_images\facialrecognition.png")
        img10 = img10.resize((550,120),Image.ANTIALIAS)
        self.photoImg10 = ImageTk.PhotoImage(img10)
        bg_lbl1=Label(bg_lbl,image=self.photoImg10)
        bg_lbl1.place(x=10,y=0,width=500,height=120)

        img11 = Image.open(r"C:\Users\Nitin\Desktop\facial recognition system\college_images\college_images\face-recognition.png")
        img11 = img11.resize((550,120),Image.ANTIALIAS)
        self.photoImg11 = ImageTk.PhotoImage(img11)
        bg_lbl22=Label(bg_lbl,image=self.photoImg11)
        bg_lbl22.place(x=515,y=0,width=500,height=120)

        img13 = Image.open(r"C:\Users\Nitin\Desktop\facial recognition system\college_images\college_images\facialrecognition.png")
        img13 = img13.resize((550,120),Image.ANTIALIAS)
        self.photoImg13 = ImageTk.PhotoImage(img13)
        bg_lbl12=Label(bg_lbl,image=self.photoImg13)
        bg_lbl12.place(x=1020,y=0,width=500,height=120)





        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=200,width=340,height=430)

        img1=Image.open(r"C:\Users\Nitin\Desktop\Login form\college_images\college_images\LoginIconAppl.png")
        img1=img1.resize((90,90),Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=200,width=90,height=90)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=85)

        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",20,"bold"),fg="white",bg="black")
        username.place(x=70,y=125)

        self.txtuser=StringVar()
        self.txtpass=StringVar()

        txtuser=ttk.Entry(frame,textvariable=self.txtuser,font=("times new roman",20,"bold"))
        txtuser.place(x=40,y=155,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",20,"bold"),fg="white",bg="black")
        password.place(x=70,y=205)

        txtpass=ttk.Entry(frame,textvariable=self.txtpass,font=("times new roman",20,"bold"))
        txtpass.place(x=40,y=240,width=270)

        # ===========Icon Image==================
        img2=Image.open(r"C:\Users\Nitin\Desktop\Login form\college_images\college_images\LoginIconAppl.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=329,width=25,height=25)

        img3=Image.open(r"C:\Users\Nitin\Desktop\Login form\college_images\college_images\lock-512.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=410,width=25,height=25)

        #login button
        loginbtn=Button(frame,text="Login",borderwidth=3,relief=RIDGE,command=self.login,font=("times new roman",15,"bold"),bd=3,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=320,width=130,height=30)

        #Register button
        registerbtn=Button(frame,text="New user Register",command=self.rgister_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=20,y=350,width=160)

        # forget Password button
        forgetbtn=Button(frame,text="Forget password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetbtn.place(x=15,y=370,width=160)

    def rgister_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="Naman" and self.txtpass.get()=="Naman@123":
            messagebox.showinfo("success","Login Successfully")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Nitin@123",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                                                                            ))

            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                        self.new_window=Toplevel(self.root)
                        self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            self.clear()
            conn.close()

    def clear(self):
        self.txtuser.set("")
        self.txtpass.set("")

    # reset pass ===========================

    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpss.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Nitin@123",database="mydata")
                my_cursor=conn.cursor()
                query=("select * from register where email=%s and securityQ=%s and securityA=%s")
                value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error ","Please enter correct answer",parent=self.root2)
                else:
                    query=("update register set password=%s where email=%s")
                    value=(self.txt_newpss.get(),self.txtuser.get())
                    my_cursor.execute(query,value)

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Info","Your Password has been reset, please login new password",parent=self.root2)
                    self.root2.destroy()
                    self.txtuser.focus()

            except Exception as es:
                messagebox.showerror("Error",f"Error Due To :{str(es)}",parent=self.root2)

     

    # forget pass ===========================

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","please enter email to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Nitin@123",database="mydata")
            my_cursor=conn.cursor()
            query=("Select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            print(row)

            if row==None:
                messagebox.showerror("My error","Please enter valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth place","Your pet name","Your nickname")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpss=ttk.Entry(font=("times new roman",15,"bold"))
                self.txt_newpss.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),bg="white",fg="green")
                btn.place(x=100,y=290)




class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # ============== variables ===================================
        

        self.var_fanme=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_SecurityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        # ==============Background image==============================
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Nitin\Desktop\Login form\college_images\college_images\pexels-roon-z-1083895.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        # left image==============================
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\Nitin\Desktop\Login form\college_images\college_images\left4.jpg")
        lt_lbl=Label(self.root,image=self.bg1)
        lt_lbl.place(x=50,y=100,width=470,height=550)


        # main frame==============================
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)


        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        # ===========label and entry ====================

        # ===========row 1 ==============================
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fanme,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)
        
        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        # =============== row 2 ================

        contact=Label(frame,text="Contact Number",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        # ========== row 3 ====================
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_SecurityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth place","Your pet name","Your nickname")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        # ========== row 4 ================

        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        # ================ check button ================

        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree the term and conditions",font=("times new roman",15,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=400)

        # ============== Button ========================
        img=Image.open(r"C:\Users\Nitin\Desktop\Login form\college_images\college_images\register-now-button1.jpg")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=50,y=470,width=200)

        img1=Image.open(r"C:\Users\Nitin\Desktop\Login form\college_images\college_images\loginpng.png")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=370,y=470,width=200)

    # Function Declaration ==========================

    def register_data(self):
        if self.var_fanme.get()=="" or self.var_email.get()=="" or self.var_SecurityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & Confirm pass must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Agree with terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Nitin@123",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already exist")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fanme.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_SecurityQ.get(),
                                                                                        self.var_SecurityA.get(),
                                                                                        self.var_pass.get()

                                                                                    ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Sucess","Register Sucessfully")
        
    def return_login(self):
        self.root.destroy()


        



if __name__=="__main__":
    main()