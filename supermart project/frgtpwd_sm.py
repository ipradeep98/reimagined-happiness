from tkinter import *
class Password:
        def frgt_pwd(self):
                try:
                    self.w.destroy()
                except:
                    pass
                self.w2=Tk()
                self.w2.title("Reset the account")
                self.w2.geometry("500x600")
                l2=Label(self.w2,font=('aria',35,'bold'),text="super",fg="red",justify="center").place(x=150,y=70)
                l2=Label(self.w2,font=('aria',35,'bold'),text="mart",fg="black").place(x=285,y=70)
                l2=Label(self.w2,font=('aria',12,'bold'),text="Better store Better living",fg="black").place(x=180,y=130)
                l2=Label(self.w2,font=('aria',10,'normal'),text="Username",bg="light grey").place(x=150,y=190)
                l2=Label(self.w2,font=('aria',10,'normal'),text="New Password",bg="light grey").place(x=150,y=230)
                l2=Label(self.w2,font=('aria',10,'normal'),text="Confirm Password",bg="light grey").place(x=150,y=270)
                self.user_name=StringVar()
                self.newpwd=IntVar()
                self.cpwd=IntVar()
                Entry(self.w2,font=('Times New Roman',12,'normal'),textvariable=self.user_name,bg="silver").place(x=280,y=190)
                Entry(self.w2,font=('Times New Roman',12,'normal'),textvariable=self.newpwd,bg="silver").place(x=280,y=230)
                Entry(self.w2,font=('Times New Roman',12,'normal'),textvariable=self.cpwd,bg="silver").place(x=280,y=270)
                b2=Button(self.w2,font=('aria',10,'normal'),text="UPDATE",bd=2,width=6,padx=2,pady=3,bg="light grey",command=self.update).place(x=230,y=310)
        def update(self):
                get_user=self.user_name.get()
                get_pwd=self.newpwd.get()
                get_cpwd=self.cpwd.get()
                print(get_user)
                print(get_pwd)
                print(get_cpwd)
                if get_user==None or get_pwd==None or get_cpwd==None:
                    l2=Label(self.w2,font=('aria',10,'normal'),text="Please fill the required inputs!!",fg="red").place(x=150,y=340)
                elif get_pwd==get_cpwd:
                    self.c.execute("USE supermart")
                    self.c.execute("UPDATE act_details set Password=('{}') WHERE Username=('{}')".format(get_cpwd,get_user))
                    l2=Label(self.w2,font=('aria',10,'normal'),text="Your account has been successfully updated!!",fg="red").place(x=150,y=340)
                elif get_pwd!=get_cpwd:
                    l2=Label(self.w2,font=('aria',10,'normal'),text="Password's doesn't match",fg="red").place(x=150,y=340)
                self.dB.commit()
#obj5=Password()
#obj5.frgt_pwd()
