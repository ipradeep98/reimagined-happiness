import pymysql
from tkinter import *
from addprod_sm import *
from prodremoval_sm import *
from priceupdate_sm import *
from addquant_sm import *
from billing_sm import *
from frgtpwd_sm import *

class Supermart(Addproducts,Removal,Update,Quantity,Password,Bill):
    def dBconnection(self):
        self.dB=pymysql.connect("localhost","root","")
        self.c=self.dB.cursor()
    def mart(self):
        self.w=Tk()
        self.w.title("SUPERMART")
        self.w.geometry("500x600")
        l=Label(self.w,font=('aria',35,'bold'),text="super",fg="red",justify="center").place(x=150,y=70)
        l=Label(self.w,font=('aria',35,'bold'),text="mart",fg="black").place(x=285,y=70)
        l=Label(self.w,font=('aria',12,'bold'),text="Better store Better living",fg="black").place(x=180,y=130)
        l=Label(self.w,font=('aria',10,'normal'),text="Username",fg="black",bg="light grey").place(x=150,y=220)
        l=Label(self.w,font=('aria',10,'normal'),text="Password",fg="black",bg="light grey").place(x=150,y=250)
        self.user=StringVar()
        self.pwd=IntVar()
        Entry(self.w,font=('Times New Roman',12,'normal'),textvariable=self.user,bg="silver").place(x=220,y=221)
        Entry(self.w,font=('Times New Roman',12,'normal'),textvariable=self.pwd,bg="silver").place(x=220,y=251)
        b=Button(self.w,font=('aria',10,'normal'),text="LOGIN",bd=2,width=5,padx=2,pady=3,bg="light grey",command=self.check).place(x=170,y=280)
        b1=Button(self.w,font=('aria',10,'normal'),text="Forgot Password?",bd=2,width=12,padx=2,pady=3,bg="light grey",command=self.frgt_pwd).place(x=240,y=280)
    def check(self):
        user_name=self.user.get()
        pwd=self.pwd.get()
        self.c.execute("USE supermart")
        self.c.execute("SELECT * from act_details WHERE username=('{}')".format(user_name))
        var=self.c.fetchone()
        if var==None:
            self.error_message() 
        elif var[0]==user_name and var[1]==pwd:
            if user_name=="admin":
                self.admin()
            elif user_name=="billing":
                self.billing()
            elif user_name=="products incharge":
                self.products()
            elif user_name=="price incharge":
                self.price()
    def error_message(self):
        w1=Tk()
        w1.title("Error message")
        w1.geometry("400x250")
        l1=Label(w1,font=('aria',11,'normal'),text="***Please give valid inputs***",fg="red").place(x=100,y=100)
    def admin(self):
        w3=Tk()
        w3.title("Admin")
        w3.geometry("500x600")
        l3=Label(w3,font=('aria',35,'bold'),text="super",fg="red",justify="center").place(x=150,y=70)
        l3=Label(w3,font=('aria',35,'bold'),text="mart",fg="black").place(x=285,y=70)
        l3=Label(w3,font=('aria',12,'bold'),text="Better store Better living",fg="black").place(x=180,y=130)
        l3=Label(w3,font=('aria',20,'bold'),text="W E L C O M E",fg="red").place(x=120,y=160)
        l3=Label(w3,font=('aria',20,'bold'),text="A D M I N",fg="black").place(x=330,y=160)
        b3=Button(w3,font=('aria',10,'normal'),text="Products",bd=2,width=6,padx=2,pady=3,bg="light grey",command=self.products).place(x=160,y=210)
        b3=Button(w3,font=('aria',10,'normal'),text="Price",bd=2,width=6,padx=2,pady=3,bg="light grey",command=self.price).place(x=240,y=210)
        b3=Button(w3,font=('aria',10,'normal'),text="Billing",bd=2,width=6,padx=2,pady=3,bg="light grey",command=self.billing).place(x=320,y=210)
    def products(self):
        w4=Tk()
        w4.title("Product list")
        w4.geometry("500x600")
        l4=Label(w4,font=('aria',35,'bold'),text="super",fg="red",justify="center").place(x=150,y=70)
        l4=Label(w4,font=('aria',35,'bold'),text="mart",fg="black").place(x=285,y=70)
        l4=Label(w4,font=('aria',12,'bold'),text="Better store Better living",fg="black").place(x=180,y=130)
        b4=Button(w4,font=('aria',10,'normal'),text="Add",bd=2,width=9,padx=2,pady=3,bg="light grey",command=self.add_products).place(x=140,y=210)
        b4=Button(w4,font=('aria',10,'normal'),text="Update",bd=2,width=9,padx=2,pady=3,bg="light grey",command=self.add_quants).place(x=240,y=210)
        b4=Button(w4,font=('aria',10,'normal'),text="Show",bd=2,width=6,padx=2,pady=3,bg="light grey",command=self.show_products).place(x=340,y=210)
        b4=Button(w4,font=('aria',10,'normal'),text="Remove",bd=2,width=6,padx=2,pady=3,bg="light grey",command=self.delete).place(x=420,y=210)
    def show_products(self):
        w7=Tk()
        w7.title("All Products")
        w7.geometry("500x600")
        title="Product ID\t\tProduct Name\t\tQuantity_Available(units)"
        l6=Label(w7,font=( 'aria' ,12, 'bold' ),text="{}".format(title),fg="black").place(x=500,y=10)            
        self.c.execute("USE supermart")
        self.c.execute("SELECT Product_id,Product_Name,Availability_in_units FROM product_details")
        yval=35
        for i in self.c:
            l6=Label(w7,font=( 'aria' ,8, 'bold' ),text="{}".format(i[0]),fg="Black").place(x=500,y=yval)
            l6=Label(w7,font=( 'aria' ,8, 'bold' ),text="{}".format(i[1]),fg="Black").place(x=720,y=yval)
            l6=Label(w7,font=( 'aria' ,8, 'bold' ),text="{}".format(i[2]),fg="Black").place(x=940,y=yval)
            yval+=30
        self.dB.commit()
    def price(self):
        w9=Tk()
        w9.title("Price")
        w9.geometry("500x600")
        l8=Label(w9,font=('aria',35,'bold'),text="super",fg="red",justify="center").place(x=150,y=70)
        l8=Label(w9,font=('aria',35,'bold'),text="mart",fg="black",justify="center").place(x=285,y=70)
        l8=Label(w9,font=('aria',12,'bold'),text="Better store Better living",fg="black").place(x=180,y=130)
        b7=Button(w9,font=('aria',10,'normal'),text="UPDATE",padx=2,pady=3,width=7,fg="black",bg="light grey",command=self.up_price).place(x=180,y=190)
        b8=Button(w9,font=('aria',10,'normal'),text="SHOW",padx=2,pady=3,width=7,fg="black",bg="light grey",command=self.show_price).place(x=260,y=190)
    def show_price(self):
        w11=Tk()
        w11.title("Product Price")
        w11.geometry("500x600")
        title="Product ID\t\tProduct Name\t\tPrice_perunit_in_Rs"
        l10=Label(w11,font=( 'aria' ,12, 'bold' ),text="{}".format(title),fg="black").place(x=500,y=10)            
        self.c.execute("USE supermart")
        self.c.execute("SELECT Product_id,Product_Name,Price_perunit_in_Rs FROM product_details")
        yval=35
        for i in self.c:
            l10=Label(w11,font=( 'aria' ,8, 'bold' ),text="{}".format(i[0]),fg="Black").place(x=500,y=yval)
            l10=Label(w11,font=( 'aria' ,8, 'bold' ),text="{}".format(i[1]),fg="Black").place(x=720,y=yval)
            l10=Label(w11,font=( 'aria' ,8, 'bold' ),text="{}".format(i[2]),fg="Black").place(x=940,y=yval)
            yval+=30
        self.dB.commit()
    def billing(self):
        w15=Tk()
        w15.title("Billing")
        w15.geometry("500x600")
        l13=Label(w15,font=('aria',35,'bold'),text="super",fg="red",justify="center").place(x=150,y=70)
        l13=Label(w15,font=('aria',35,'bold'),text="mart",fg="black",justify="center").place(x=285,y=70)
        l13=Label(w15,font=('aria',12,'bold'),text="Better store Better living",fg="black").place(x=180,y=130)
        b20=Button(w15,font=('aria',10,'normal'),text="Bill",padx=2,pady=3,width=7,fg="black",bg="light grey",command=self.bill_data).place(x=180,y=190)
        b21=Button(w15,font=('aria',10,'normal'),text="SHOW",padx=2,pady=3,width=7,fg="black",bg="light grey",command=self.show_bill).place(x=260,y=190)
    def show_bill(self):
        w14=Tk()
        w14.title("Billing data")
        w14.geometry("500x600")
        title="Bill ID\t\tCustomer name\t\tbill amount\t\tdate"
        l12=Label(w14,font=( 'aria' ,12, 'bold' ),text="{}".format(title),fg="black").place(x=500,y=10)
        self.c.execute("USE supermart")
        self.c.execute("SELECT Bill_id,Customer_Name,Total_amount_in_Rs,date FROM bill_data")
        yval=35
        for i in self.c:
            l12=Label(w14,font=( 'aria' ,8, 'bold' ),text="{}".format(i[0]),fg="Black").place(x=500,y=yval)
            l12=Label(w14,font=( 'aria' ,8, 'bold' ),text="{}".format(i[1]),fg="Black").place(x=650,y=yval)
            l12=Label(w14,font=( 'aria' ,8, 'bold' ),text="{}".format(i[2]),fg="Black").place(x=870,y=yval)
            l12=Label(w14,font=( 'aria' ,8, 'bold' ),text="{}".format(i[3]),fg="Black").place(x=1000,y=yval)
            yval+=30
        self.dB.commit()
        
obj=Supermart()
obj.dBconnection()
obj.mart()

