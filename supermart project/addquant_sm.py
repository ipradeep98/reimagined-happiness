from tkinter import *
class Quantity:
    def add_quants(self):
        try:
            self.w.destroy()
        except:
            pass
        self.w6=Tk()
        self.w6.title("Update")
        self.w6.geometry("500x600")
        l5=Label(self.w6,font=('aria',35,'bold'),text="super",fg="red",justify="center").place(x=150,y=70)
        l5=Label(self.w6,font=('aria',35,'bold'),text="mart",fg="black").place(x=285,y=70)
        l5=Label(self.w6,font=('aria',12,'bold'),text="Better store Better living",fg="black").place(x=180,y=130)
        l5=Label(self.w6,font=('aria',10,'normal'),text="Product ID",bg="light grey").place(x=140,y=210)
        l5=Label(self.w6,font=('aria',10,'normal'),text="Quantity to add",bg="light grey").place(x=140,y=240)
        self.pro_id=IntVar()
        self.pro_addquant=IntVar()
        Entry(self.w6,font=('Times New Roman',12,'normal'),textvariable=self.pro_id,bg="silver").place(x=260,y=210)
        Entry(self.w6,font=('Times New Roman',12,'normal'),textvariable=self.pro_addquant,bg="silver").place(x=260,y=240)
        b5=Button(self.w6,font=('aria',10,'normal'),text="OK",bg="light grey",command=self.update1).place(x=230,y=280)
    def update1(self):
        prod_id=self.pro_id.get()
        quant=self.pro_addquant.get()
        if prod_id!=None and quant!=None:
            self.c.execute("USE supermart")
            self.c.execute("SELECT Availability_in_units from product_details WHERE Product_id=('{}')".format(prod_id))
            d=self.c.fetchone()
            up_quant=d[0]+quant
            self.c.execute("UPDATE product_details set Availability_in_units=('{}')WHERE Product_id=('{}')".format(up_quant,prod_id))
            l5=Label(self.w6,font=('aria',10,'normal'),text="Quantity has been successfully updated!!",fg="red").place(x=140,y=320)
        else:
            l5=Label(self.w6,font=('aria',10,'normal'),text="Please fill the valid inputs!!",fg="red").place(x=140,y=320)
        self.dB.commit()
        self.pro_id.set(0)
        self.pro_addquant.set(0)
#obj3=Quantity()
#obj3.add_quants()
