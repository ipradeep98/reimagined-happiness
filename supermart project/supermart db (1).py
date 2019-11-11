import pymysql
import datetime
import os
dB=pymysql.connect("localhost","root","")
c=dB.cursor()

c.execute("create database supermart")
c.execute("use supermart")
c.execute("create table act_details(Username varchar(50),Password int)")
c.execute("create table product_details(Product_id int,Product_Name varchar(50),Availability_in_units int,Price_perunit_in_Rs int)")
c.execute("create table bill_data(Bill_id int,Customer_Name varchar(50),Contact_number bigint,Total_amount_in_Rs int,date varchar(50))")

c.execute("Insert into act_details values('admin',1234)")
c.execute("Insert into act_details values('billing',2345)")
c.execute("Insert into act_details values('products incharge',3456)")
c.execute("Insert into act_details values('price incharge',6789)")

c.execute("Insert into product_details values(100,'Frooti(200ml)',40,20)")
date2=datetime.datetime.today()
c.execute("Insert into bill_data values(1,'consumer name',8220478569,20,('{}'))".format(date2))

fldr=os.mkdir("billing files")
print(os.getcwd())
os.chdir("E:\supermart project\\billing files")
f=open("Readme.txt",'x')
f=open("Readme.txt",'w')
f.write("\t\t\tDescription\n\tThis folder contains all the customer details which is involved with Bill ID,Customer Name,Contact Number,Total Price and Date of the bill")
f.close()
dB.commit()
c.close()
