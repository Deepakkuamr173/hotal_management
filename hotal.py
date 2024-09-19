
from tkinter import *
import os 
from PIL import Image, ImageTk  # Ensure Pillow is installed: pip install pillow

from customer2 import cust_win
from room import Roombooking



class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")  # Use 'x' to separate width and height

        # .......................Header Image.............
    
        img1 = Image.open(r"D:\TOP.jpg")
        # img1 = img1.resize((1550, 140), Image.ANTIALIAS)
        img1 = img1.resize((1550, 140), Image.LANCZOS)

    
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        # Create a label with the image
        header_img = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        header_img.place(x=0, y=0, width=1550, height=140)  

        # ................Logo.....................
        img2 = Image.open(r"D:\logo.png.jpeg")
        img2 = img2.resize((210, 140), Image.LANCZOS)#antialia use here befor
        self.photoimg2 = ImageTk.PhotoImage(img2) # Convert the image to PhotoImage
        
        # Create a label with the image
        logo_img = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        logo_img.place(x=0, y=0, width=210, height=140)  

        #...............title..........
        lb1_title = Label(
        self.root,
        text="HOTEL MANAGEMENT SYSTEM",  
        font=("Times New Roman", 40, "bold"),  
        bg="black",  
        fg="gold",  
        bd=4,  
        relief=RIDGE 
        )
        # Place the label in the window
        lb1_title.place(x=0, y=140, width=1550, height=50)  

        #............ main fram.......................
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        # ......menu..........
        lb1_menu = Label(
        main_frame,
        text="MENU",  # Correct argument name and text
        font=("Times New Roman", 20, "bold"),  # Correct font family name and style
        bg="black",  # Background color
        fg="gold",  # Correct color name
        bd=4,  # Border width
        relief=RIDGE  # Border style
        )
        # Place the label in the window
        lb1_menu.place(x=0, y=0, width=230)  


        #............ button fram.......................
        button_frame=Frame(main_frame,bd=4,relief=RIDGE)
        button_frame.place(x=0,y=35,width=228,height=190)

        cust_button=Button(button_frame,text="CUSTOMER",
        command=self.cust_deetails,                    
        font=("Times New Roman", 14, "bold"),  
        bg="black",  
        fg="gold",   
        bd=0,
        width=22,
        cursor="hand1" 
        )
        cust_button.grid(row=0,column=0,pady=1)


        room_button=Button(button_frame,text="ROOM", 
        command=self.roombooking,                                    
        font=("Times New Roman", 14, "bold"),  
        bg="black",  
        fg="gold",   
        bd=0,
        width=22,
        cursor="hand1" 
        )
        room_button.grid(row=1,column=0,pady=1)


        details_button=Button(button_frame,text="DETAILS",                   
        font=("Times New Roman", 14, "bold"),  
        bg="black",  
        fg="gold",   
        bd=0,
        width=22,
        cursor="hand1" 
        )
        details_button.grid(row=2,column=0,pady=1)


        report_button = Button(button_frame, text="REPORT",                   
        font=("Times New Roman", 14, "bold"),  
        bg="black",  
        fg="gold",   
        bd=0,
        width=22,
        cursor="hand1" 
        )
        report_button.grid(row=3, column=0,pady=1)

        logout_button = Button(button_frame, text="LOGOUT",                   
        font=("Times New Roman", 14, "bold"),  
        bg="black",  
        fg="gold",   
        bd=0,
        width=22,
        cursor="hand1" 
        )
        logout_button.grid(row=4, column=0,pady=1)



        # .............right side image.............
        img3 = Image.open(r"D:\right1.png.jpg")
        img3 = img3.resize((1310, 590), Image.LANCZOS) #ANTIALIAS use befor than after use
        self.photoimg3 = ImageTk.PhotoImage(img3) # Convert the image to PhotoImage
        
        lb1mg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lb1mg1.place(x=225, y=0, width=1310, height=590) 

        # ............duwn image 1 .................................
        img4 = Image.open(r"D:\view.png")
        img4 = img4.resize((230, 210), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4) # Convert the image to PhotoImage
        
        lb1mg2 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lb1mg2.place(x=0, y=225, width=230, height=210)

        #............down image2 .................................. 
        img5 = Image.open(r"D:\khana.png")
        img5 = img5.resize((230,190), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5) # Convert the image to PhotoImage
        
        lb1mg3 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lb1mg3.place(x=0, y=420, width=230, height=190)


    #............for window button...............
    def cust_deetails(self):
        self.new_window=Toplevel(self.root)
        self.app=cust_win(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window) 
     

       
        
if __name__ == "__main__":
    root = Tk()
    app = HotelManagementSystem(root)
    root.mainloop()
