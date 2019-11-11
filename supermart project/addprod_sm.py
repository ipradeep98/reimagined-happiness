from tkinter import *
class Addproducts:
    def add_products(self):
        try:
            self.w.destroy()
        except:
            pass
        self.w5=Tk()
        self.w5.title("New Product")
        self.w5.geometry("500x600")
        l5=Label(self.w5,font=('aria',35,'bold'),text="super",fg="red",justify="center").place(x=150,y=70)
        l5=Label(self.w5,font=('aria',35,'bold'),text="mart",fg="black").place(x=285,y=70)
        l5=Label(self.w5,font=('aria',12,'bold'),text="Better store Better living",fg="black").place(x=180,y=130)
        l5=Label(self.w5,font=('aria',10,'normal'),text="Product Name",bg="light grey").place(x=140,y=210)
        l5=Label(self.w5,font=('aria',10,'normal'),text="No.of units",bg="light grey").place(x=140,y=240)
        l5=Label(self.w5,font=('aria',10,'normal'),text="Price",bg="light grey").place(x=140,y=270)
        self.pro_name=StringVar()
        self.pro_quants=IntVar()
        self.pro_price=IntVar()
        Entry(self.w5,font=('Times New Roman',12,'normal'),textvariable=self.pro_name,bg="silver").place(x=260,y=210)
        Entry(self.w5,font=('Times New Roman',12,'normal'),textvariable=self.pro_quants,bg="silver").place(x=260,y=240)
        Entry(self.w5,font=('Times New Roman',12,'normal'),textvariable=self.pro_price,bg="silver").place(x=260,y=270)
        b5=Button(self.w5,font=('aria',10,'normal'),text="OK",bg="light grey",command=self.update).place(x=230,y=320)
    def update(self):
        pr_name=self.pro_name.get()
        pr_qua=self.pro_quants.get()
        pr_pri=self.pro_price.get()
        if pr_name!=None and pr_qua!=None and pr_pri!=None:
            self.c.execute("USE supermart")
            self.c.execute("SELECT Product_id FROM product_details order by Product_id DESC limit 1")
            var=self.c.fetchone()
            prod_id=var[0]+1
            self.c.execute("INSERT into product_details values('{}','{}','{}','{}')".format(prod_id,pr_name,pr_qua,pr_pri))
            l5=Label(self.w5,font=('aria',10,'normal'),text="Product has been successfully added!!",fg="red").place(x=140,y=350)
        else:
            l5=Label(self.w5,font=('aria',10,'normal'),text="Please fill the valid inputs!!",fg="red").place(x=140,y=320)
        self.dB.commit()
        self.pro_name.set("")
        self.pro_quants.set(0)
        self.pro_price.set(0)
#obj4=Addproducts()
#obj4.add_products()
