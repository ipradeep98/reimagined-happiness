from tkinter import *
class Update:
    def up_price(self):
        try:
            self.w.destroy()
        except:
            pass
        self.w10=Tk()
        self.w10.title("Add price")
        self.w10.geometry("500x600")
        l9=Label(self.w10,font=('aria',35,'bold'),text="super",fg="red",justify="center").place(x=150,y=70)
        l9=Label(self.w10,font=('aria',35,'bold'),text="mart",fg="black",justify="center").place(x=285,y=70)
        l9=Label(self.w10,font=('aria',12,'bold'),text="Better store Better living",fg="black").place(x=180,y=130)
        l9=Label(self.w10,font=('aria',10,'normal'),text="Product ID",fg="black",bg="light grey").place(x=150,y=170)
        l9=Label(self.w10,font=('aria',10,'normal'),text="New amount",fg="black",bg="light grey").place(x=150,y=210)
        self.pro_id1=IntVar()
        self.amt=IntVar()
        Entry(self.w10,font=('Times New Roman',12,'normal'),textvariable=self.pro_id1,bg="silver").place(x=260,y=170)
        Entry(self.w10,font=('Times New Roman',12,'normal'),textvariable=self.amt,bg="silver").place(x=260,y=210)
        b9=Button(self.w10,font=('aria',10,'normal'),text="OK",padx=2,pady=3,width=3,fg="black",command=self.updation).place(x=230,y=250)
    def updation(self):
        prod_id1=self.pro_id1.get()
        price=self.amt.get()
        #if prod_id1=None and price!=None:
        self.c.execute("USE supermart")
        self.c.execute("SELECT Price_perunit_in_Rs from product_details WHERE Product_id=('{}')".format(prod_id1))
        c=self.c.fetchone()
        up_price=c[0]+price
        self.c.execute("UPDATE product_details set Price_perunit_in_Rs=('{}')WHERE Product_id=('{}')".format(up_price,prod_id1))
        l9=Label(self.w10,font=('aria',10,'normal'),text="Price has been successfully updated!!",fg="red").place(x=150,y=290)
        #else:
            #l9=Label(self.w10,font=('aria',10,'normal'),text="Enter the input correctly!!",fg="red").place(x=150,y=290)
        self.dB.commit()
        self.pro_id1.set(0)
        self.amt.set(0)
#obj1=Update()
#obj1.up_price()
