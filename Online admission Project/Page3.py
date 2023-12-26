from tkinter import*
from tkinter import messagebox
from Page4 import Last_page
class Third_page:
    def __init__(self,window,cur,con,i):
        """All the wotking of this page is ame ,Just table Name is different and data is for Intermediate -_-"""
        self.i=i
        self.window=window
        self.cur=cur
        self.con=con
        self.third_page()
        self.radio_buttons()
    def radio_buttons(self):
        # Variable to store the selected option
        self.selected_option = StringVar()  ##This call will make an inside variable to associate it with a value
        # Create Radio buttons
        self.radio_button1 = Radiobutton(self.window, text="A Grade", variable=self.selected_option, value="A",
                                         command=self.on_radio_button_click)
        self.radio_button2 = Radiobutton(self.window, text="Other's", variable=self.selected_option, value="B",
                                         command=self.on_radio_button_click)
        self.radio_button1.grid(row=7, column=1)
        self.radio_button2.grid(row=8, column=1)
        self.radio_button4 = Radiobutton(self.window, text="1st Division", variable=self.selected_option, value="1",
                                         command=self.on_radio_click1)
        self.radio_button5 = Radiobutton(self.window, text="2nd Division", variable=self.selected_option, value="2",
                                         command=self.on_radio_click1)
        self.radio_button4.grid(row=7, column=3)
        self.radio_button5.grid(row=8, column=3)
    def on_radio_button_click(self):
        self.selected_value = self.selected_option.get()
        self.entrys9.delete(0, END)  # Clear the entry
        self.entrys9.insert(0, self.selected_value)  # Insert the selected value
    def on_radio_click1(self):
        self.selected_value = self.selected_option.get()
        self.entrys10.delete(0, END)  # Clear the entry
        self.entrys10.insert(0, self.selected_value)
    def create_canvas(self):
        self.canvas = Canvas(width=200, height=200)
        self.image1 = PhotoImage(file="logo2.png")
        self.canvas.create_image(100, 100, image=self.image1)
        self.canvas.grid(column=1, row=1,columnspan=3)
    def next_page(self):
        if self.data3():
            self.insert_data()
            for widget in self.window.winfo_children():#all the wigets inside that window get destroyed thorugh winfo_children() and destroy
                widget.destroy()
                self.create_canvas()
                self.page4()
    def page4(self):
        self.last=Last_page(cur=self.cur,con=self.con,window=self.window)
    def data3(self):
        self.list3=[]
        self.list3.clear()
        self.Board3=self.entrys1.get()
        self.degree_title3=self.entrys2.get()
        self.exam_type3=self.entrys3.get()
        self.passing_year3=self.entrys4.get()
        self.roll_no3=self.entrys5.get()
        self.regestration_no3=self.entrys6.get()
        self.total_marks3=self.entrys7.get()
        self.obtained_marks3=self.entrys8.get()
        self.grade3=self.entrys9.get()
        self.division3=self.entrys10.get()
        self.list3+=self.Board3,self.degree_title3,self.exam_type3,self.passing_year3,self.roll_no3,self.regestration_no3,self.total_marks3,self.obtained_marks3,self.grade3,self.division3
        is_empty=False
        for i in self.list3:
             if i=="":
                 is_empty=True
        if is_empty:
            messagebox.showinfo(title="Data Error", message="Don't leave any field empty")
            return False
        return True
    def insert_data(self):
        """This will try to create table if doesnot exist and then add data by calling add_data() mthod if table elready exist """
        try:
            self.cur.execute("CREATE TABLE DATA3 (id SERIAL PRIMARY KEY,BOARD TEXT,DEGREE"
                         "TEXT,EXAM_TYPE TEXT,PASSING_YEAR TEXT,ROLL_NO TEXT,REGESTRATION_NO TEXT,TOTAL_MARKS TEXT,OBTAINED_MARKS TEXT,GRADE TEXT,DIVISION TEXT)")
        except:
            self.add_data()
        else:
            self.add_data()
    def add_data(self):
        """This method will add data into the table"""
        self.tupe = (self.i,self.Board3,self.degree_title3,self.exam_type3,self.passing_year3,self.roll_no3,self.regestration_no3,self.total_marks3,self.obtained_marks3,self.grade3,self.division3)
        self.cur.execute(f"INSERT INTO DATA3 VALUES {self.tupe}")
        self.con.commit()
        pass
    def hsoe(self):
        """This method will printn the data from the table but only for the admin use please"""
        self.cur.execute(f"SELECT * FROM DATA3")
        r = self.cur.fetchall()
        for i1 in r:
            print()
            for j in i1:
                print(j)
    def third_page(self):
        """This will creates all the entries,labels,buttons for the third page :)"""
        self.label12=Label()
        # self.label12.grid(column=0, row=10, columnspan=5, padx=10)
        self.label12 = Label(text="(Intermediate -_-)")
        FONT_NAME = "Courier"
        self.label12.config(font = (FONT_NAME, 15, "bold"))
        self.label12.grid(column=1, row=1)
        # Label1 and Enrty1
        self.labels1 = Label()
        self.labels1.config(text="Board University :")
        self.labels1.grid(column=0, row=2, pady=10)
        self.entrys1 = Entry(width=33)
        self.entrys1.grid(column=1, row=2)
        # Label2 and Entery2
        self.labels2 = Label()
        self.labels2.config(text="Degree Title :")
        self.labels2.grid(column=2, row=2, pady=10)
        self.entrys2 = Entry(width=33)
        self.entrys2.grid(column=3, row=2)
        # Label3 and Entry3
        self.labels3 = Label()
        self.labels3.config(text="Exam Type :")
        self.labels3.grid(column=0, row=3)
        self.entrys3 = Entry(width=33)
        self.entrys3.grid(column=1, row=3, pady=10)
        # label4 and Entry4
        self.labels4 = Label()
        self.labels4.config(text="Passing Year :")
        self.labels4.grid(column=2, row=3)
        self.entrys4 = Entry(width=33)
        self.entrys4.grid(column=3, row=3, pady=10)
        # label5 and Entry5
        self.labels5 = Label()
        self.labels5.config(text="Roll  NO: ")
        self.labels5.grid(column=0, row=4)
        self.entrys5 = Entry(width=33)
        self.entrys5.grid(column=1, row=4, pady=10)
        # label6 and Entry6
        self.labels6 = Label()
        self.labels6.config(text="Regestration No: ")
        self.labels6.grid(column=2, row=4)
        self.entrys6 = Entry(width=33)
        self.entrys6.grid(column=3, row=4, pady=10)
        # Entery7 and label7
        self.labels7 = Label()
        self.labels7.config(text="Total Marks :")
        self.labels7.grid(column=0, row=5)
        self.entrys7 = Entry(width=33)
        self.entrys7.grid(column=1, row=5, pady=10)
        # Entery8 and label8
        self.labels8 = Label()
        self.labels8.config(text="Obtained Marks")
        self.labels8.grid(column=2, row=5)
        self.entrys8 = Entry(width=33)
        self.entrys8.grid(column=3, row=5, pady=10)
        # Entery9 and label9
        self.labels9 = Label()
        self.labels9.config(text="Grade :")
        self.labels9.grid(column=0, row=6)
        self.entrys9 = Entry(width=33)
        self.entrys9.grid(column=1, row=6, pady=10)
        # Entery10 and label10
        self.labels10 = Label()
        self.labels10.config(text="Division :")
        self.labels10.grid(column=2, row=6)
        self.entrys10 = Entry(width=33)
        self.entrys10.grid(column=3, row=6, pady=10)
        self.label111 = Label()
        self.label111.config(
            text="     \n\t\t  _____________________________________________________________________________________________________")
        self.label111.grid(column=0, row=10, columnspan=5, padx=10)
        self.button1 = Button()
        self.button1.config(text="Proceed", width=33, command=self.next_page)
        self.button1.grid(column=2, row=13, pady=10)
        self.label18 = Label()
        self.label18.config(text="")
        self.label18.grid(column=1, row=13)
        self.radio_buttons()