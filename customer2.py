from tkinter import *
from PIL import Image, ImageTk 

from tkinter import ttk
import random
import tkinter as tk

import mysql.connector

from tkinter import messagebox
import sys
'''First, we have to import the sys module in our program 
before running any functions. sys.modules. This function provides the name
 of the existing python modules which have been imported.'''

import re  # provides regular expression suppor and  Regular expressions are a powerful language for matching text patterns.
class cust_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #...........variable..........
        self.var_ref = tk.StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()
        self.var_address =StringVar()

    




        #...............title..........
        lb1_title = Label(
        self.root,
        text="ADD CUSTOMER DETAILS",  
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

    

#...............label fram...........
        LabelFrameleft = LabelFrame(
        self.root,
        relief=RIDGE,  # Only need to specify this once
        text="Customer Details",
        font=("Times New Roman", 12, "bold"),
        bg="white",
        fg="gold",
        bd=5
        )
        LabelFrameleft.place(x=5, y=50, width=425, height=490)

#...........label and entry key.............
        lb1_cust_ref = Label(LabelFrameleft, text="Customer Ref:", font=("arial", 12, "bold"), padx=2, pady=6)
        lb1_cust_ref.grid(row=0, column=0, sticky=tk.W)

        Entry_ref = ttk.Entry(LabelFrameleft, textvariable=self.var_ref, widt=29, font=("arial", 13, "bold"),state="readonly")
        Entry_ref.grid(row=0, column=1)

        # .........customer name..................
        cust_name_ref = Label(LabelFrameleft, text="Customer Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        cust_name_ref.grid(row=1, column=0, sticky=tk.W)
        
        # name=self.var_cust_name.get()
        # if name=="":
        #    messagebox.showerror("Error","Please enter the mobile number",parent=self.root)
        # elif not name.isalpha():
        #    messagebox.showerror("Error","name must contain only alphabet",parent=self.root)   
        

        cname_ref = ttk.Entry(LabelFrameleft, textvariable=self.var_cust_name, width=29, font=("arial", 13, "bold"))
        cname_ref.grid(row=1, column=1)

        # ...........mother name.............
        mother_ref = tk.Label(LabelFrameleft, text="Mother Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        mother_ref.grid(row=2, column=0, sticky=tk.W)

        mname_ref = ttk.Entry(LabelFrameleft, textvariable=self.var_mother, width=29, font=("arial", 13, "bold"))
        mname_ref.grid(row=2, column=1)

        # ............gender........................
        gender_cust_ref = tk.Label(LabelFrameleft, text="Gender:", font=("arial", 12, "bold"), padx=2, pady=6)
        gender_cust_ref.grid(row=3, column=0, sticky=tk.W)

        combo_gender = ttk.Combobox(LabelFrameleft, textvariable=self.var_gender, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_gender["value"] = ("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)
        
        # ..............postcode............................
        cpost_code_ref = tk.Label(LabelFrameleft, text="Post Code:", font=("arial", 12, "bold"), padx=2, pady=6)
        cpost_code_ref.grid(row=4, column=0, sticky=tk.W)

        post_ref = ttk.Entry(LabelFrameleft, textvariable=self.var_post, width=29, font=("arial", 13, "bold"))
        post_ref.grid(row=4, column=1)

        # .......mobile number...........
        mobile_ref = tk.Label(LabelFrameleft, text="Mobile Number:", font=("arial", 12, "bold"), padx=2, pady=6)
        mobile_ref.grid(row=5, column=0, sticky=tk.W)

        cmobile_ref = ttk.Entry(LabelFrameleft, textvariable=self.var_mobile, width=29, font=("arial", 13, "bold"))
        cmobile_ref.grid(row=5, column=1)

        # ........email...........
        email_ref = tk.Label(LabelFrameleft, text="Email ID:", font=("arial", 12, "bold"), padx=2, pady=6)
        email_ref.grid(row=6, column=0, sticky=tk.W)

        cemail_ref = ttk.Entry(LabelFrameleft, textvariable=self.var_email, width=29, font=("arial", 13, "bold"))
        cemail_ref.grid(row=6, column=1)

        # ........nationality............
        nationality_ref = tk.Label(LabelFrameleft, text="Nationality:", font=("arial", 12, "bold"), padx=2, pady=6)
        nationality_ref.grid(row=7, column=0, sticky=tk.W)

        combo_nationality = ttk.Combobox(LabelFrameleft, textvariable=self.var_nationality, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_nationality["value"] = ("India", "Nepal", "Pakistan")
        combo_nationality.current(0)
        combo_nationality.grid(row=7, column=1)

        # .....id proof type combo box
        cid_ref = tk.Label(LabelFrameleft, text="ID Proof:", font=("arial", 12, "bold"), padx=2, pady=6)
        cid_ref.grid(row=8, column=0, sticky=tk.W)

        combo_id = ttk.Combobox(LabelFrameleft, textvariable=self.var_id_proof, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_id["value"] = ("Aadhar Card", "Driving Licence", "Passport")
        combo_id.current(0)
        combo_id.grid(row=8, column=1)

        # ........id number...........
        idnumber_ref = tk.Label(LabelFrameleft, text="ID Number:", font=("arial", 12, "bold"), padx=2, pady=6)
        idnumber_ref.grid(row=9, column=0, sticky=tk.W)

        cidnumber_ref = ttk.Entry(LabelFrameleft, textvariable=self.var_id_number, width=29, font=("arial", 13, "bold"))
        cidnumber_ref.grid(row=9, column=1)

        # ........address...........
        address_ref = tk.Label(LabelFrameleft, text="Address:", font=("arial", 12, "bold"), padx=2, pady=6)
        address_ref.grid(row=10, column=0, sticky=tk.W)

        caddress_ref = ttk.Entry(LabelFrameleft, textvariable=self.var_address, width=29, font=("arial", 13, "bold"))
        caddress_ref.grid(row=10, column=1)

        # ...........button......
        btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=38)
        
        btnadd=Button(btn_frame,text="Add",command=self.add_date,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnadd.grid(row=0,column=0,padx=1)


        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btndelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnreset.grid(row=0,column=3,padx=1)

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
        table_frame.place(x=419, y=50, width=875, height=490)

        lb1searchBy=Label(table_frame,text="Search By :",font=("arial", 12, "bold"),bg="red",fg="white")
        lb1searchBy.grid(row=0,column=0,sticky=W,padx=2)
        
        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial", 12, "bold"),width=27,state="readonly")
        combo_search["value"]=("Mobile number","Driving licence","Passport","ref")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.text_search=StringVar()
        csearch=ttk.Entry(table_frame,width=29,textvariable=self.text_search,font=("arial",10,"bold"))
        csearch.grid(row=0,column=2,padx=2)

        bsearch=Button(table_frame,text="Search",command=self.search,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        bsearch.grid(row=0,column=3,padx=2)

        bshowall=Button(table_frame,text="Show all",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        bshowall.grid(row=0,column=4,padx=2)
        

        #........show data table.........

        details_table = Frame(
        table_frame,
        relief=RIDGE,  # Only need to specify this once
        bd=2
        )
        details_table.place(x=0, y=50, width=860, height=350)

        Scrol_x = ttk.Scrollbar(details_table, orient=tk.HORIZONTAL)
        Scrol_y = ttk.Scrollbar(details_table, orient=tk.VERTICAL)

# Create the Treeview widget with columns
        self.cust_details_table = ttk.Treeview(
        details_table,
        columns=("ref", "name", "mother", "gender", "post", "mobile", "email", "nationality", "idproof", "idnumber", "address"),
        xscrollcommand=Scrol_x.set,
        yscrollcommand=Scrol_y.set
        )

# Pack the scrollbars and associate them with the Treeview
        Scrol_x.pack(side=BOTTOM, fill=X)
        Scrol_y.pack(side=RIGHT, fill=Y)

        Scrol_x.config(command=self.cust_details_table.xview)
        Scrol_y.config(command=self.cust_details_table.yview)


        # Define the headings for each column
        self.cust_details_table.heading("ref", text="Refer No")
        self.cust_details_table.heading("name", text="Name")
        self.cust_details_table.heading("mother", text="Mother's Name")
        self.cust_details_table.heading("gender", text="Gender")
        self.cust_details_table.heading("post", text="Post")
        self.cust_details_table.heading("mobile", text="Mobile No")
        self.cust_details_table.heading("email", text="Email ID")
        self.cust_details_table.heading("nationality", text="Nationality")
        self.cust_details_table.heading("idproof", text="ID Proof")
        self.cust_details_table.heading("idnumber", text="ID Number")
        self.cust_details_table.heading("address", text="Address")

        # Configure the Treeview to display only the headings
        self.cust_details_table["show"] = "headings"


        # Set the width of the columns
        self.cust_details_table.column("ref", width=100)
        self.cust_details_table.column("name", width=100)
        self.cust_details_table.column("mother", width=150)  # You can adjust this as needed
        self.cust_details_table.column("gender", width=80)
        self.cust_details_table.column("post", width=100)
        self.cust_details_table.column("mobile", width=100)
        self.cust_details_table.column("email", width=150)
        self.cust_details_table.column("nationality", width=100)
        self.cust_details_table.column("idproof", width=100)
        self.cust_details_table.column("idnumber", width=120)
        self.cust_details_table.column("address", width=200)
        # Pack the Treeview to fill the space in the frame
        self.cust_details_table.pack(fill=tk.BOTH, expand=1)
        self.cust_details_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()
    
# from tkinter import messagebox

    def add_date(self):
      if self.var_mobile.get() == "" or self.var_mother.get() == "":
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

            # Correct SQL INSERT statement
            sql = """
            INSERT INTO customer2 (
                ref, name, mother, gender, postcose, mobile, email, nationality, IDproof, `ID number`, `Address`
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            my_cursor.execute(sql, (
                self.var_ref.get(),
                self.var_cust_name.get(),
                self.var_mother.get(),
                self.var_gender.get(),
                self.var_post.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_id_proof.get(),
                self.var_id_number.get(),
                self.var_address.get()
            ))

            conn.commit()
            self.fetch_data()
            conn.close()

            messagebox.showinfo("Success", "Customer has been added", parent=self.root)
        except Exception as es:
           
            messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
    # data show in customer data base table 
    def fetch_data(self):
       
        conn= mysql.connector.connect(
                host="localhost",
                username="root",
                password="Deepak@7632",
                database="deepak2"
            )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer2")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
           self.cust_details_table.delete(*self.cust_details_table.get_children())
           for i in rows:
              self.cust_details_table.insert("",END,values=i)

           conn.commit()
        conn.close() 
# show all the data in customer_details_table
    def get_cursor(self,event=""):
       cursor_row=self.cust_details_table.focus()
       content=self.cust_details_table.item(cursor_row)
       row=content["values"]


       self.var_ref.set(row[0]),        
       self.var_cust_name.set(row[1]),        
       self.var_mother.set(row[2]),        
       self.var_gender.set (row[3]),        
       self.var_post.set (row[4]),        
       self.var_mobile.set (row[5]),        
       self.var_email.set (row[6]),        
       self.var_nationality.set (row[7]),        
       self.var_id_proof.set (row[8]),        
       self.var_id_number.set (row[9]),        
       self.var_address.set (row[10])
#  update customer data

    def update(self):
    # Check if mobile number is entered
      if self.var_mobile.get() == "":
        messagebox.showerror("Error", "Please enter the mobile number", parent=self.root)

      elif not re.match(r'^\d{10}$', self.var_mobile.get()): 
        messagebox.showerror("Error", "please enter the mobile number 10 digits", parent=self.root)  
# name only alphabet required
    #   elif self.var_cust_name=="":
    #        messagebox.showerror("Error","Please enter the mobile number",parent=self.root)
    #   elif not self.var_cust_name.isalpha():
    #        messagebox.showerror("Error","name must contain only alphabet",parent=self.root)    
      else: 
        try:
            # Establish database connection
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Deepak@7632",
                database="deepak2"
            )
            my_cursor = conn.cursor()

            # Execute the update query
            my_cursor.execute("""update customer2 set Name=%s, mother=%s, Gender=%s, postcose=%s, Mobile=%s, Email=%s, nationality=%s, IDproof=%s, `ID number`=%s, `Address`=%s 
                where ref=%s
            """, (
                self.var_cust_name.get(),
                self.var_mother.get(),
                self.var_gender.get(),
                self.var_post.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_id_proof.get(),
                self.var_id_number.get(),
                self.var_address.get(),
                self.var_ref.get()
            ))

            # Commit the transaction
            conn.commit()

            # Refresh the data in the UI after update
            self.fetch_data()

            # Close the database connection
            conn.close()

            # Show success message
            messagebox.showinfo("update", "Customer details have been updated successfully", parent=self.root)
        
        except Exception as es:
            # Handle exceptions
            messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
# work on delete button
    def delete(self):
       delete=messagebox.askyesno("Hotal management system","do you delete this customer",parent=self.root)
       if delete>0:
          
          conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Deepak@7632",
                database="deepak2"
            )
          my_cursor = conn.cursor()
          query="delete from customer2 where ref=%s"
          value=(self.var_ref.get(),)
          my_cursor.execute(query,value)
       else:
          if not delete:
             return
       conn.commit()
       self.fetch_data()
       conn.close()
# work on reset button 
    def reset(self):
        
    #    self.var_ref.set(row[0]),        
        self.var_cust_name.set(""),        
        self.var_mother.set(""),        
    #    self.var_gender.set (row[3]),        
        self.var_post.set (""),        
        self.var_mobile.set (""),        
        self.var_email.set (""),        
    #    self.var_nationality.set (row[7]),        
    #    self.var_id_proof.set (row[8]),        
        self.var_id_number.set (""),        
        self.var_address.set ("")

        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

    # import mysql.connector

    def search(self):
        try:
    # Establish connection to the MySQL database
         conn = mysql.connector.connect(
         host="localhost",
         user="root",
         password="Deepak@7632",
         database="deepak2"
          ) 
    
         my_cursor = conn.cursor()

    # Safely create the SQL query using a parameterized query to prevent SQL injection
         query = "SELECT * FROM customer2 WHERE " + str(self.search_var.get()) + " LIKE %s"
         value = "%" + str(self.text_search.get()) + "%"
    
         my_cursor.execute(query, (value,))
         rows = my_cursor.fetchall()

    # Clear the table before inserting new data
         if len(rows) != 0:
           self.cust_details_table.delete(*self.cust_details_table.get_children())
           for row in rows:
            self.cust_details_table.insert("", "end", values=row)
    
    # Commit the transaction and close the connection
         conn.commit()
        except mysql.connector.Error as err:
          print(f"Error: {err}")

        finally:
         conn.close()


    
           
        

           
          
          
              

       

if __name__=="__main__":
    root=Tk()
    obj=cust_win(root)
    root.mainloop()      





