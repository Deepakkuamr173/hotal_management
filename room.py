
from tkinter import *
from PIL import Image, ImageTk 

from tkinter import ttk
import random
import tkinter as tk

import mysql.connector

from tkinter import messagebox
import sys
import re  # provides regular expression support

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #  .........variable.........
        self.var_contact=StringVar()
        self.var_checkindade=StringVar()
        self.var_checkoutdade=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailabe=StringVar()
        self.var_meal=StringVar()
        self.var_noofday=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
         
        lb1_title = Label(
            self.root,
            text="ROOM BOOKINGS",  
            font=("Times New Roman", 18, "bold"),  
            bg="black",  
            fg="gold",  
            bd=4,  
            relief=RIDGE 
        )
        lb1_title.place(x=0, y=0, width=1295, height=50)  

        # ................Logo.....................
        img2 = Image.open(r"D:\logo.png.jpeg")
        img2 = img2.resize((60, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2) # Convert the image to PhotoImage 
        # Create a label with the image
        logo_img = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        logo_img.place(x=0, y=0, width=60, height=50)
  
        # ...............label frame...........
        LabelFrameleft = LabelFrame(
            self.root,
            relief=RIDGE,  
            text="Room booking",
            font=("Times New Roman", 12, "bold"),
            bg="white",
            fg="red",
            bd=5
        )
        LabelFrameleft.place(x=5, y=50, width=425, height=490)
        
#...........label and entry key.............
# ...........customer contect.........
        lb1_cust_contect = Label(LabelFrameleft, text="Customer contect:", font=("arial", 12, "bold"), padx=2, pady=6)
        lb1_cust_contect.grid(row=0, column=0, sticky=tk.W)

        Entry_contect = ttk.Entry(LabelFrameleft, widt=17,textvariable=self.var_contact, font=("arial", 13, "bold"))
        Entry_contect.grid(row=0, column=1,sticky=W)
          
# .........fetch data button.....
        btnfetchdata=Button(LabelFrameleft,text="Fetch Data",command=self.fetch_contect,font=("arial",10,"bold"),bg="black",fg="gold",width=8)
        btnfetchdata.place(x=322,y=4)


#...........check in date.............
        ccheck_in_data = Label(LabelFrameleft, text="check in date:", font=("arial", 12, "bold"), padx=2, pady=6)
        ccheck_in_data.grid(row=1, column=0, sticky=tk.W)

        ccheck_in_data = ttk.Entry(LabelFrameleft, widt=29,textvariable=self.var_checkindade, font=("arial", 13, "bold"))
        ccheck_in_data.grid(row=1, column=1)

#...........check out date.............

        lb1_check_out = Label(LabelFrameleft, text="check_out date:", font=("arial", 12, "bold"), padx=2, pady=6)
        lb1_check_out.grid(row=2, column=0, sticky=tk.W)

        lb1_check_out = ttk.Entry(LabelFrameleft, widt=29,textvariable=self.var_checkoutdade, font=("arial", 13, "bold"))
        lb1_check_out.grid(row=2, column=1)

#...........room type.............

        lb1_roomtype = Label(LabelFrameleft, text="Room type:", font=("arial", 12, "bold"), padx=2, pady=6)
        lb1_roomtype.grid(row=3, column=0, sticky=tk.W)
        lb1_roomtype = ttk.Entry(LabelFrameleft, widt=29,textvariable=self.var_roomtype ,font=("arial", 13, "bold"))
        lb1_roomtype.grid(row=3, column=1)

        combo_gender = ttk.Combobox(LabelFrameleft, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_gender["value"] = ("Single", "Double", "laxary")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

#...........Availabe.............

        lb1_roomAvailabe= Label(LabelFrameleft, text="Room Availabe:", font=("arial", 12, "bold"), padx=2, pady=6)
        lb1_roomAvailabe.grid(row=4, column=0, sticky=tk.W)
        lb1_roomAvailabe = ttk.Entry(LabelFrameleft, widt=29,textvariable=self.var_roomavailabe ,font=("arial", 13, "bold"))
        lb1_roomAvailabe.grid(row=4, column=1)

#...........Meal.............

        lb1_Meal = Label(LabelFrameleft, text="Meal:", font=("arial", 12, "bold"), padx=2, pady=6)
        lb1_Meal.grid(row=5, column=0, sticky=tk.W)
        lb1_Meal = ttk.Entry(LabelFrameleft, widt=29,textvariable=self.var_meal, font=("arial", 13, "bold"))
        lb1_Meal.grid(row=5, column=1)

#...........no of day.............

        lb1noofday = Label(LabelFrameleft, text="No of day:", font=("arial", 12, "bold"), padx=2, pady=6)
        lb1noofday.grid(row=6, column=0, sticky=tk.W)
        lb1noofday = ttk.Entry(LabelFrameleft, widt=29,textvariable=self.var_noofday, font=("arial", 13, "bold"))
        lb1noofday.grid(row=6, column=1)

#...........Paid tex.............

        lb1_Paidtex = Label(LabelFrameleft, text="Paid tex:", font=("arial", 12, "bold"), padx=2, pady=6)
        lb1_Paidtex.grid(row=7, column=0, sticky=tk.W)
        lb1_Paidtex = ttk.Entry(LabelFrameleft, widt=29,textvariable=self.var_paidtax, font=("arial", 13, "bold"))
        lb1_Paidtex.grid(row=7, column=1)        

#...........Sub total.............

        lb1_Subtotal = Label(LabelFrameleft, text="Sub total:", font=("arial", 12, "bold"), padx=2, pady=6)
        lb1_Subtotal.grid(row=8, column=0, sticky=tk.W)
        lb1_Subtotal = ttk.Entry(LabelFrameleft, widt=29, textvariable=self.var_actualtotal,font=("arial", 13, "bold"))
        lb1_Subtotal.grid(row=8, column=1)


#........... Total Cost.............

        lb1_TotalCost = Label(LabelFrameleft, text="Total Cost:", font=("arial", 12, "bold"), padx=2, pady=6)
        lb1_TotalCost.grid(row=9, column=0, sticky=tk.W)
        lb1_TotalCost = ttk.Entry(LabelFrameleft, widt=29,textvariable=self.var_total, font=("arial", 13, "bold"))
        lb1_TotalCost.grid(row=9, column=1)

# ...........bill button###################################
        btnbill=Button(LabelFrameleft,text="Bill",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnbill.grid(row=10,column=0,padx=1,sticky=W)


        # ...........button............
        # btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
        # btn_frame.place(x=0,y=400,width=412,height=38)
        
        # btnadd=Button(btn_frame,text="Add",command=self.add_date,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        # btnadd.grid(row=0,column=0,padx=1)

        btn_frame = Frame(LabelFrameleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=38)

        btnadd = Button(btn_frame, text="Add", command=self.add_date, font=("arial", 12, "bold"), 
                bg="black", fg="gold", width=9)
        btnadd.grid(row=0, column=0, padx=1)



        btnupdate=Button(btn_frame,text="Update",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="Delete",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btndelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="Reset",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnreset.grid(row=0,column=3,padx=1)
# ..............write image............

        img2 = Image.open(r"D:\bed.png")
        img2 = img2.resize((550, 190), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img2) # Convert the image to PhotoImage 
        # Create a label with the image
        logo_img = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        logo_img.place(x=765, y=55, width=550, height=190)


#    ...table fram and search system.........
        table_frame = LabelFrame(
        self.root,
        relief=RIDGE,  # Only need to specify this once
        text="View details and search system ",
        font=("Times New Roman", 12, "bold"),
        bg="white",
        fg="gold",
        bd=5
        )
        table_frame.place(x=430, y=245, width=860, height=290)

        lb1searchBy=Label(table_frame,text="Search By :",font=("arial", 12, "bold"),bg="red",fg="white")
        lb1searchBy.grid(row=0,column=0,sticky=W,padx=2)
        
        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial", 12, "bold"),width=27,state="readonly")
        combo_search["value"]=("contect","Room")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.text_search=StringVar()
        csearch=ttk.Entry(table_frame,width=29,textvariable=self.text_search,font=("arial",10,"bold"))
        csearch.grid(row=0,column=2,padx=2)

        bsearch=Button(table_frame,text="Search",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        bsearch.grid(row=0,column=3,padx=2)

        bshowall=Button(table_frame,text="Show all",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        bshowall.grid(row=0,column=4,padx=2)


        #........show data table.........

        details_table = Frame(
        table_frame,
        relief=RIDGE,  # Only need to specify this once
        bd=2
        )
        details_table.place(x=0, y=50, width=860, height=216)

        Scrol_x = ttk.Scrollbar(details_table, orient=tk.HORIZONTAL)
        Scrol_y = ttk.Scrollbar(details_table, orient=tk.VERTICAL)

# Create the Treeview widget with columns
        self.room_table = ttk.Treeview(
        details_table,
        columns=("Contact", "checkindate", "checkoutdate", "Roomtype", "Roomavailabe", "Meal", "noofday"),
        xscrollcommand=Scrol_x.set,
        yscrollcommand=Scrol_y.set
        )

# Pack the scrollbars and associate them with the Treeview
        Scrol_x.pack(side=BOTTOM, fill=X)
        Scrol_y.pack(side=RIGHT, fill=Y)

        Scrol_x.config(command=self.room_table.xview)
        Scrol_y.config(command=self.room_table.yview)


        # Define the headings for each column
        self.room_table.heading("Contact", text="Contact No")
        self.room_table.heading("checkindate", text="check in date")
        self.room_table.heading("checkoutdate", text="check out date")
        self.room_table.heading("Roomtype", text="Room type")
        self.room_table.heading("Roomavailabe", text="Room Availabe")
        self.room_table.heading("Meal", text="Meal")
        self.room_table.heading("noofday", text="No of day")
        # Configure the Treeview to display only the headings
        self.room_table["show"] = "headings"
        # Set the width of the columns
        self.room_table.column("Contact", width=100)
        self.room_table.column("checkindate", width=100)
        self.room_table.column("checkoutdate", width=150)  # You can adjust this as needed
        self.room_table.column("Roomtype", width=80)
        self.room_table.column("Roomavailabe", width=100)
        self.room_table.column("Meal", width=100)
        self.room_table.column("noofday", width=150)
        # Pack the Treeview to fill the space in the frame
        self.room_table.pack(fill=tk.BOTH, expand=1)

        self.fetch_data()
   

    def add_date(self):
       if self.var_contact.get() == "" or self.var_checkindate.get() == "":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
       else:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Deepak@7632",
                database="deepak2"
            )
            my_cursor = conn.cursor()

            sql = """
                INSERT INTO room 
                (Contact, checkin, checkout, roomtype, `room availabe`, meal, Noofday)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
            # Execute the query by passing the values in the tuple
            my_cursor.execute(sql, (
                self.var_contact.get(),
                self.var_checkindate.get(),  # Corrected variable name
                self.var_checkoutdate.get(),  # Corrected variable name
                self.var_roomtype.get(),
                self.var_roomavailabe.get(),
                self.var_meal.get(),
                self.var_noofday.get()
            ))

            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Customer has been added", parent=self.root)
        except mysql.connector.Error as err:
            messagebox.showwarning("Warning", f"Database error: {err}", parent=self.root)
        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
        finally:
            if conn.is_connected():
                conn.close()

    def fetch_data(self):
       
        try:
            conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="Deepak@7632",
            database="deepak2"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM room")
            rows = my_cursor.fetchall()

            if len(rows) != 0:
              self.room_table.delete(*self.room_table.get_children())  # Corrected table name
              for i in rows:
                self.room_table.insert("", END, values=i)

            conn.commit()  
        except mysql.connector.Error as err:
         messagebox.showwarning("Warning", f"Database error: {err}", parent=self.root)
        finally:
          conn.close()



#     def add_date(self):
#       if self.var_contact.get() == "" or self.var_checkindate.get() == "":
#          messagebox.showerror("Error", "All fields are required", parent=self.root)
#       else:
#         try:
            
#             conn = mysql.connector.connect(
#                 host="localhost",
#                 username="root",
#                 password="Deepak@7632",
#                 database="deepak2"
#             )
#             my_cursor = conn.cursor()

#             sql = """
#                 INSERT INTO room 
#                 (Contact, checkin, checkout, roomtype, `room availabe`, meal, Noofday)
#                 VALUES (%s, %s, %s, %s, %s, %s, %s)
#                 """

#             # Execute the query by passing the values in the tuple
#             my_cursor.execute(sql, (
#                 self.var_contact.get(),
#                 self.var_checkindade.get(),
#                 self.var_checkoutdade.get(),
#                 self.var_roomtype.get(),
#                 self.var_roomavailabe.get(),
#                 self.var_meal.get(),
#                 self.var_noofday.get()
#                 ))

#             conn.commit()
#         #     self.fetch_data()
#             conn.close()

#             messagebox.showinfo("Success", "Customer has been added", parent=self.root)
#         except Exception as es:
#          messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

#     def fetch_data(self):
       
#         conn= mysql.connector.connect(
#                 host="localhost",
#                 username="root",
#                 password="Deepak@7632",
#                 database="deepak2"
#             )
#         my_cursor = conn.cursor()
#         my_cursor.execute("select * from room")
#         rows=my_cursor.fetchall()
#         if len(rows)!=0:
#            self.room_table.delete(*self.cust_details_table.get_children())
#            for i in rows:
#               self.room_table.insert("",END,values=i)

#            conn.commit()
#         conn.close()





    #...............all data fetch..............
    def fetch_contect(self):
     if self.var_contact.get() == "":
        messagebox.showerror("Error", "Please enter the contact number", parent=self.root)
     else:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Deepak@7632",
                database="deepak2"
            )
            my_cursor = conn.cursor()

            query = "SELECT name FROM customer2 WHERE `Mobile` = %s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "This number is not found", parent=self.root)
            else:
                showdataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showdataframe.place(x=445, y=55, width=300, height=180)

                lblname = Label(showdataframe, text="Name:", font=("arial", 12, "bold"))
                lblname.place(x=0, y=0)

                lbl = Label(showdataframe, text=row[0], font=("arial", 12, "bold"))
                lbl.place(x=90, y=0)

             #....gender......
                conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Deepak@7632",
                database="deepak2"
                )
                my_cursor = conn.cursor()

                query = "SELECT gender FROM customer2 WHERE `Mobile` = %s"
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblgender = Label(showdataframe, text="Gender:", font=("arial", 12, "bold"))
                lblgender.place(x=0, y=30)

                lbl2 = Label(showdataframe, text=row[0], font=("arial", 12, "bold"))
                lbl2.place(x=100, y=30)
                   
                   #.......email.........
                conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Deepak@7632",
                database="deepak2"
                )
                my_cursor = conn.cursor()

                query = "SELECT email FROM customer2 WHERE `Mobile` = %s"
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblemail = Label(showdataframe, text="Email:", font=("arial", 12, "bold"))
                lblemail.place(x=0, y=50)

                lbl3 = Label(showdataframe, text=row[0], font=("arial", 12, "bold"))
                lbl3.place(x=90, y=50)


        #        #.....nationality........
                conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Deepak@7632",
                database="deepak2"
                )
                my_cursor = conn.cursor()

                query = "SELECT nationality FROM customer2 WHERE `Mobile` = %s"
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblnationality = Label(showdataframe, text="Nationality:", font=("arial", 12, "bold"))
                lblnationality.place(x=0, y=80)

                lbl3 = Label(showdataframe, text=row[0], font=("arial", 12, "bold"))
                lbl3.place(x=100, y=80)

               #.......address.....................
                conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Deepak@7632",
                database="deepak2"
                )
                my_cursor = conn.cursor()

                query = "SELECT address FROM customer2 WHERE `Mobile` = %s"
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lbladdress = Label(showdataframe, text="Address:", font=("arial", 12, "bold"))
                lbladdress.place(x=0, y=110)

                lbl3 = Label(showdataframe, text=row[0], font=("arial", 12, "bold"))
                lbl3.place(x=100, y=110)



        



            conn.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Something went wrong: {err}", parent=self.root)
            if conn.is_connected():
                conn.close()

if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()
