from tkinter import *
class Removal:
    def delete(self):
        try:
            self.w.destroy()
        except:
            pass
        self.w8=Tk()
        self.w8.title("Remove Product")
        self.w8.geometry("500x600")
        l7=Label(self.w8,font=('aria',35,'bold'),text="super",fg="red",justify="center").place(x=150,y=70)
        l7=Label(self.w8,font=('aria',35,'bold'),text="mart",fg="black",justify="center").place(x=285,y=70)
        l7=Label(self.w8,font=('aria',12,'bold'),text="Better store Better living",fg="black").place(x=180,y=130)
        l7=Label(self.w8,font=('aria',10,'normal'),text="Product ID",fg="black",bg="light grey").place(x=150,y=180)
        self.id2=IntVar()
        Entry(self.w8,font=('aria',10,'normal'),textvariable=self.id2,fg="black",bg="light grey").place(x=230,y=180)
        b6=Button(self.w8,font=('aria',10,'normal'),text="OK",padx=2,pady=3,width=3,fg="black",command=self.update2).place(x=200,y=220)
    def update2(self):
        prod_id2=self.id2.get()
        if prod_id2!=None:
            self.c.execute("USE supermart")
            self.c.execute("DELETE from product_details WHERE Product_id=('{}')".format(prod_id2))
            l7=Label(self.w8,font=('aria',10,'normal'),text="Product has been removed!!",fg="red").place(x=150,y=260)
        else:
            l7=Label(self.w8,font=('aria',10,'normal'),text="Enter the input correctly!!",fg="red").place(x=150,y=260)
        self.dB.commit()
        self.id2.set(0)
#obj2=Removal()
#obj2.delete()
