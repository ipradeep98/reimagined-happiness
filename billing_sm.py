import pymysql
import datetime
from tkinter import *
import os
from tkinter import messagebox
class Bill:
    def connection(self):
        self.dB=pymysql.connect("localhost","root","")
        self.c=self.dB.cursor()
    def bill_data(self):
        try:
            self.w.destroy()
        except:
            pass
        self.w12=Tk()
        self.w12.title("BILLING")
        self.w12.geometry("500x600")
        l11=Label(self.w12,font=('aria',35,'bold'),text="super",fg="red",justify="center").place(x=150,y=70)
        l11=Label(self.w12,font=('aria',35,'bold'),text="mart",fg="black",justify="center").place(x=285,y=70)
        l11=Label(self.w12,font=('aria',12,'bold'),text="Better store Better living",fg="black").place(x=180,y=130)
        l11=Label(self.w12,font=('aria',10,'bold'),text="Product ID",fg="black",bg="light grey").place(x=160,y=170)
        l11=Label(self.w12,font=('aria',10,'bold'),text="Quantity",fg="black",bg="light grey").place(x=160,y=210)
        self.bpid=IntVar()
        self.bqua=IntVar()
        Entry(self.w12,font=('aria',12,'normal'),bg="light grey",textvariable=self.bpid).place(x=280,y=170)
        Entry(self.w12,font=('aria',12,'normal'),bg="light grey",textvariable=self.bqua).place(x=280,y=210)
        l11=Label(self.w12,font=('aria',10,'bold'),text="Customer Name",fg="black",bg="light grey").place(x=160,y=250)
        l11=Label(self.w12,font=('aria',10,'bold'),text="Contact number",fg="black",bg="light grey").place(x=160,y=290)
        self.cusname=StringVar()
        self.cusnum=IntVar()
        Entry(self.w12,font=('aria',12,'normal'),bg="light grey",textvariable=self.cusname).place(x=280,y=250)
        Entry(self.w12,font=('aria',12,'normal'),bg="light grey",textvariable=self.cusnum).place(x=280,y=290)
        b10=Button(self.w12,font=('aria',10,'bold'),text="Add",fg="black",padx=3,pady=4,width=3,command=self.addprice).place(x=200,y=350)
        b11=Button(self.w12,font=('aria',10,'bold'),text="Total",fg="black",padx=3,pady=4,width=3,command=self.total).place(x=270,y=350)
        self.total=0
        self.lqua=[]
        self.lid=[]
        self.lpri=[]
    def addprice(self):
        self.adpid=self.bpid.get()
        self.adqua=self.bqua.get()
        if self.adpid!=None and self.adqua!=None:
            self.c.execute("USE supermart")
            self.c.execute("SELECT Product_id,Availability_in_units from product_details WHERE Product_id='{}'".format(self.adpid))
            det=self.c.fetchone()
            if det[0]==None:
                messagebox.showinfo("Error","ProductID unavailable")
            elif det[1]<self.adqua:
                messagebox.showinfo("Error","Quantity Insufficient")
        self.lid.append(self.adpid)
        self.lqua.append(self.adqua)
        self.c.execute("USE supermart")
        self.c.execute("SELECT Price_perunit_in_Rs from product_details WHERE Product_id='{}'".format(self.adpid))
        det1=self.c.fetchone()
        self.price=det1[0]*self.adqua
        self.lpri.append(self.price)
        self.total=sum(self.lpri)
        self.bpid.set(0)
        self.bqua.set(0)
    def total(self):
        l11=Label(self.w12,font=('aria',35,'bold'),text="super",fg="red",justify="center").place(x=150,y=70)
        l11=Label(self.w12,font=('aria',35,'bold'),text="mart",fg="black",justify="center").place(x=285,y=70)
        l11=Label(self.w12,font=('aria',12,'bold'),text="Better store Better living",fg="black").place(x=180,y=130)
        txt="Product\t\t\t\t\tPrice\t\tQuantity\t\t\tCost"
        l11=Label(self.w12,font=('aria',10,'bold'),text="{}".format(txt),fg="black",bg="light grey").place(x=160,y=390)
        yval=420
        for i in range (len(self.lid)):
            self.c.execute("USE supermart")
            self.c.execute("SELECT Availability_in_units from product_details WHERE Product_id='{}'".format(self.adpid))
            x=self.c.fetchone()
            self.update=x[0]-self.adqua
            self.c.execute("UPDATE product_details set Availability_in_units='{}' WHERE Product_id='{}'".format(self.update,self.adpid))
            self.dB.commit()
            self.c.execute("USE supermart")
            self.c.execute("SELECT Product_id,Price_perunit_in_Rs from product_details WHERE Product_id='{}'".format(self.lid[i]))
            y=self.c.fetchone()
            print(y)
            l11=Label(self.w12,font=('aria',10,'normal'),text="{}".format(y[0]),bg="light grey").place(x=162,y=yval)
            l11=Label(self.w12,font=('aria',10,'normal'),text="{}".format(y[1]),bg="light grey").place(x=442,y=yval)
            l11=Label(self.w12,font=('aria',10,'normal'),text="{}".format(self.lqua[i]),bg="light grey").place(x=580,y=yval)
            l11=Label(self.w12,font=('aria',10,'normal'),text="{}".format(self.lpri[i]),bg="light grey").place(x=730,y=yval)
            yval+=35
        l11=Label(self.w12,font=('aria',10,'bold'),text="Total: {}".format(self.total),bg="light grey").place(x=350,y=yval)
        b11=Button(self.w12,font=('aria',10,'bold'),text="Print",fg="black",padx=3,pady=4,width=3,command=self.yesorno).place(x=270,y=yval+70)
    def yesorno(self):
        self.w13=Tk()
        self.w13.title("PRINT")
        self.w13.geometry("225x150")
        Label(self.w13,font=( 'aria' ,16, 'bold' ),text=" Confirm Print?",fg="Black",justify="center").place(x=30,y=20)
        Button(self.w13,padx=16,pady=8, bd=5 ,fg="black",font=('ariel' ,10,'bold'),width=2, text="Yes", bg="light Grey",command=self.printbill).place(x=40,y=70)
        Button(self.w13,padx=16,pady=8, bd=5 ,fg="black",font=('ariel' ,10,'bold'),width=2, text="No", bg="light Grey",command=self.w13.destroy).place(x=110,y=70)
    def printbill(self):
        self.cname=self.cusname.get()
        self.cnum=self.cusnum.get()
        self.c.execute("USE supermart")
        self.c.execute("SELECT Bill_id from bill_data order by Bill_id desc limit 1")
        z=self.c.fetchone()
        self.date1=datetime.datetime.today()
        self.c.execute("INSERT into bill_data values ('{}','{}','{}','{}','{}')".format(z[0]+1,self.cname,self.cnum,self.total,self.date1))
        self.dB.commit()
        title=("\t\t\t\tS U P E R M  A  R  T\n")
        head=("\t\tProduct_Name\t\tPrice/Quantity\t\tCost")
        d1=self.cname
        d2=self.cnum
        d3=self.date1
        os.chdir("E:\supermart project\\billing files")
        f1=open("{}.txt".format(z[0]+1),'x')
        f1=open("{}.txt".format(z[0]+1),'w')
        f1.write("\n\tCustomer Name: {}\tCustomer number: {}\tBilldate: {}".format(d1,d2,d3))
        f1.write("\n\n{}\n{}".format(title,head))
        f1.close()
        for i in range(len(self.lid)):
            self.c.execute("USE supermart")
            self.c.execute("SELECT Product_id,Price_perunit_in_Rs from product_details WHERE Product_id='{}'".format(self.lid[i]))
            q=self.c.fetchone()
            e1=("\t\t{}\t\t{}".format(q[0],q[1]))
            e2=("{}".format(self.lpri[i]))
            f2=open("{}.txt".format(z[0]+1),'a')
            f2.write("\n\n{}\t\t\t{}".format(e1,e2))
            f2.close()
        print()
        d4=("\t\t\t\tTotal:{}".format(self.total))
        f3=open("{}.txt".format(z[0]+1),'a')
        f3.write("\n\n{}".format(d4))
        f3.close()
        self.cusname.set("")
        self.cusnum.set("")
        
#obj=Bill()
#obj.connection()
#obj.billing()


        
