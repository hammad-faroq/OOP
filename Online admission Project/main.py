from tkinter import*
from tkinter import messagebox
from Page2 import Second_page
import sqlite3
class Admission:
    def __init__(self):
        self.con=sqlite3.connect("application.db")
        self.cur=self.con.cursor()
        self.window = Tk()
        self.window.title("Admission Form")
        self.window.config(padx=30, pady=50)
        self.window.minsize(890,800)
        self.create_canvas()
        self.main_page()
    def create_canvas(self):
        """This method  will create canvas for the window"""
        self.canvas = Canvas(width=200, height=200)
        self.image1 = PhotoImage(file="logo2.png")
        self.canvas.create_image(100, 100, image=self.image1)
        self.canvas.grid(column=1, row=1,columnspan=3)
    def on_radio_button_click(self):
        """This method is the  working of radio button Blood Group"""
        self.selected_value = self.selected_option.get()
        self.entry9.delete(0, END)  # Clear the entry
        self.entry9.insert(0, self.selected_value)  # Insert the selected value
    def on_radio_click1(self):
        """This method is the working of mariatal status"""
        self.selected_value = self.selected_option.get()
        self.entry10.delete(0, END)  # Clear the entry
        self.entry10.insert(0, self.selected_value)

    def next_page(self):
        """This method will create next page by deleting all the widgets in the first page"""
        if self.data():
            self.insert_data()
            for widget in self.window.winfo_children():#all the wigets inside that window get destroyed thorugh winfo_children() and destroy
                widget.destroy()
            self.create_canvas()
            self.second_page()
    def insert_data(self):
        """this function will try to create the table and insert data into the table if already exist Table_Name(DATA) """
        try:
            self.cur.execute("CREATE TABLE DATA (id SERIAL PRIMARY KEY,NAME TEXT,CNIC TEXT,FATHER_NAME TEXT,"
                             "FATHER_CNIC TEXT,FATHER_OCCUPATION TEXT,GENDER TEXT,DATE_OF_BIRTH TEXT,"
                             "BLOOD_GROUP TEXT,MARIATAL_STATUS TEXT,RELIGION TEXT,HAFIZ TEXT,MOBILE_NO TEXT,GUARDIAN_CONTACT_NO TEXT,EMAIL TEXT,PROVINCE TEXT")
        except:
            self.add_date()
        else:
            self.add_date()
    def add_date(self):
        try:##This is done to store the id into a file(If there is no file it will create it and stores 1 in it)
            ###This is done to handle the exception and to keep track of the unique id for the table
            with open(file="record.txt",mode="r") as file:
                data=file.readline()
                actual=int(data)
        except:
            with open(file="record.txt",mode="w") as file:
                file.write("1")
            self.i=1
        else:
            self.i=actual
        finally:
            self.tupe = (
            self.i,self.name,self.cnic,self.father_name, self.father_cnic, self.father_occu, self.gender, self.dob, self.blood_group,
            self.mariatal_status, self.religion, self.hafiz, self.mobile_no, self.guardian_contact_no, self.email,
            self.province)
            self.cur.execute(f"INSERT INTO DATA VALUES {self.tupe}")
            self.con.commit()
            self.i+=1
            da=str(self.i)
            self.i=int(self.i)
            self.i-=1
            with open(file="record.txt", mode="w") as file:
                file.write(da)
    def hsoe(self):
        """This method will show the data from the table but not available for the user :)"""
        self.cur.execute(f"SELECT * FROM DATA")
        r = self.cur.fetchall()
        for i1 in r:
            print()
            for j in i1:
                print(str(j).strip(), end=" ")
        print()
    def second_page(self):
        """This method  will create second page from the class SECOND_PAGE :)"""
        self.second_pag=Second_page(self.window,cur=self.cur,con=self.con,i=self.i)
    def on_checkbox_click(self):
        """This check box is for the working of HAFIz-e-QURAN ENRTY"""
        # self.entry12.config(f"{'Yes' if self.check_var.get() else 'No'}")##what the heck is :)
        if self.check_var.get():
            self.entry12.delete(0,END)
            self.entry12.insert(0,"Yes")
        else:
            self.entry12.delete(0, END)
            self.entry12.insert(0, "No")
    def data(self):
        """This method will return true is all the entries have some values else false"""
        self.list=[]
        self.list.clear()
        self.cnic=self.entry1.get()
        self.cnic1=self.entry2.get()
        self.name=self.entry3.get()
        self.father_name=self.entry4.get()
        self.father_occu=self.entry5.get()
        self.father_cnic=self.entry6.get()
        self.gender=self.entry7.get()
        self.dob=self.entry8.get()
        self.blood_group=self.entry9.get()
        self.mariatal_status=self.entry10.get()
        self.religion=self.entry11.get()
        self.hafiz = self.entry12.get()
        self.mobile_no = self.entry13.get()
        self.guardian_contact_no = self.entry14.get()
        self.email = self.entry15.get()
        self.province = self.entry16.get()
        self.list+=self.name,self.father_name,self.father_occu,self.father_cnic,self.gender,self.dob,self.blood_group,self.mariatal_status,self.religion,self.hafiz,self.mobile_no,self.guardian_contact_no,self.email,self.province
        if f"{self.cnic}"==f"{self.cnic1}":
            pass
        else:
            messagebox.showinfo(title="Data Error",message="CNIC Don't Match")
            return False
        is_empty=False
        for i in self.list:
             if i=="" or i=='13/01/2023':
                 is_empty=True
        if is_empty:
            messagebox.showinfo(title="Data Error", message="Don't leave any field empty")
            return False
        return True

    def on_checkbox_click1(self):
        """This method is for the working of the check_box of islam"""
        # self.entry12.config(f"{'Yes' if self.check_var.get() else 'No'}")##what the heck is :)
        if self.check_var1.get():
            self.entry11.delete(0,END)
            self.entry11.insert(0,"Islam")
        else:
            self.entry11.delete(0, END)
            self.entry11.insert(0, "Other's")
    def main_page(self):
        """This method will create all the widgets that are show on the front page"""
        # Label1 and Enrty1
        self.label1 = Label()
        self.label1.config(text="Enter CNIC :")
        self.label1.grid(column=0, row=2,pady=10)
        self.entry1 = Entry(width=33)
        self.entry1.grid(column=1, row=2)
        # Label2 and Entery2
        self.label2 = Label()
        self.label2.config(text="Retype CNIC :")
        self.label2.grid(column=2, row=2,pady=10)
        self.entry2 = Entry(width=33)
        self.entry2.insert(0, "xx-xx")
        # data_website = entry1.get()
        self.entry2.grid(column=3, row=2)
        # Label3 and Entry3
        self.label3 = Label()
        self.label3.config(text="Name :")
        self.label3.grid(column=0, row=3)
        self.entry3 = Entry(width=33)
        self.entry3.grid(column=1, row=3,pady=10)
        # label4 and Entry4
        self.label4 = Label()
        self.label4.config(text="Father Name: ")
        self.label4.grid(column=2, row=3)
        self.entry4 = Entry(width=33)
        self.entry4.grid(column=3, row=3, pady=10)
        # label5 and Entry5
        self.label5 = Label()
        self.label5.config(text="Father Occupation: ")
        self.label5.grid(column=0, row=4)
        self.entry5 = Entry(width=33)
        self.entry5.grid(column=1, row=4, pady=10)
        # label6 and Entry6
        self.label6 = Label()
        self.label6.config(text="Father CNIC: ")
        self.label6.grid(column=2, row=4)
        self.entry6 = Entry(width=33)
        self.entry6.grid(column=3, row=4, pady=10)
        # Entery7 and label7
        self.label7 = Label()
        self.label7.config(text="Gender (M or F): ")
        self.label7.grid(column=0, row=5)
        self.entry7 = Entry(width=33)
        self.entry7.grid(column=1, row=5,pady=10)
        # Entery8 and label8
        self.label8 = Label()
        self.label8.config(text="Date of Birth")
        self.label8.grid(column=2, row=5)
        self.entry8 = Entry(width=33)
        self.entry8.insert(0,"13/01/2023")
        self.entry8.grid(column=3, row=5, pady=10)
        # Entery9 and label9
        self.label9 = Label()
        self.label9.config(text="Blood Group: ")
        self.label9.grid(column=0, row=6)
        self.entry9 = Entry(width=33)
        self.entry9.grid(column=1, row=6, pady=10)
        # Entery10 and label10
        self.label10 = Label()
        self.label10.config(text="Marital Status :")
        self.label10.grid(column=2, row=6)
        self.entry10 = Entry(width=33)
        self.entry10.grid(column=3, row=6, pady=10)
        # Entery11 and label11
        self.label11 = Label()
        self.label11.config(text="Religion :")
        self.label11.grid(column=2, row=9)
        self.entry11 = Entry(width=33)
        # self.entry11.insert(0,"Islam")
        self.entry11.grid(column=3, row=9, pady=10)
        self.radio_buttons()
        # Entery12 and label12
        self.label12 = Label()
        self.label12.config(text="Hafiz-e-Quran :")
        self.label12.grid(column=0, row=9)
        self.entry12 = Entry(width=33)
        self.entry12.grid(column=1, row=9, pady=10)
        self.label111=Label()
        self.label111.config(text="     \n\t\t  _____________________________________________________________________________________________________")
        self.label111.grid(column=0,row=10,columnspan=5,padx=10)
        #Entry and label 13
        self.label13 = Label()
        self.label13.config(text="Mobile No :")
        self.label13.grid(column=0, row=11)
        self.entry13 = Entry(width=33)
        self.entry13.grid(column=1, row=11, pady=10)
        # Entry and label 14
        self.label14 = Label()
        self.label14.config(text="Guardian Contact No :")
        self.label14.grid(column=2, row=11)
        self.entry14 = Entry(width=33)
        self.entry14.grid(column=3, row=11, pady=10)
        # Entry and label 15
        self.label15 = Label()
        self.label15.config(text="Email Address :")
        self.label15.grid(column=0, row=12)
        self.entry15 = Entry(width=33)
        self.entry15.grid(column=1, row=12, pady=10)
        # Entry and label 16
        self.label16 = Label()
        self.label16.config(text="Province :")
        self.label16.grid(column=2, row=12)
        self.entry16 = Entry(width=33)
        self.entry16.grid(column=3, row=12, pady=10)
        self.button1=Button()
        self.button1.config(text="Next Page",width=33,command=self.next_page)
        self.button1.grid(column=2,row=13,pady=10)
        self.label18 = Label()
        self.label18.config(text="")
        self.label18.grid(column=1, row=13)
        self.radio_buttons()
        self.check_box()
        self.check_box1()
        self.main_loop()
    def main_loop(self):
        """This method will continuously check for the events in the GUI"""
        self.window.mainloop()
    def check_box(self):
        """This is the Hafiz check box"""
        self.check_var=BooleanVar()
        self.check_bex=Checkbutton(text="Yes",variable=self.check_var,command=self.on_checkbox_click)
        self.check_bex.grid(column=1,row=10)
    def check_box1(self):
        """THis is the Religion (islam) check box"""
        self.check_var1=BooleanVar()
        self.check_bex1=Checkbutton(text="Islam",variable=self.check_var1,command=self.on_checkbox_click1)
        self.check_bex1.grid(column=3,row=10)
    def radio_buttons(self):
        """Htis method will create 4 radio buttons for the Bood group and Mariatal status :)"""
        # Variable to store the selected option
        self.selected_option = StringVar()##This call will make an inside variable to associate it with a value
        # Create Radio buttons
        self.radio_button1 = Radiobutton(self.window, text="A Category", variable=self.selected_option,value="A Category",command=self.on_radio_button_click)
        self.radio_button2 = Radiobutton(self.window, text="B Category", variable=self.selected_option,value="B Category",command=self.on_radio_button_click)
        self.radio_button1.grid(row=7, column=1)
        self.radio_button2.grid(row=8, column=1)
        self.radio_button4 = Radiobutton(self.window, text="Married", variable=self.selected_option,value="Married", command=self.on_radio_click1)
        self.radio_button5 = Radiobutton(self.window, text="Single :)", variable=self.selected_option,value="Single", command=self.on_radio_click1)
        self.radio_button4.grid(row=7, column=3)
        self.radio_button5.grid(row=8, column=3)
a=Admission()
