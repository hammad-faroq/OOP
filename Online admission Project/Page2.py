from tkinter import*
from tkinter import messagebox
from Page3 import Third_page
class Second_page:
    def __init__(self,window,con,cur,i):
        """The Constructor will reqrire the connection and cursor of the previous data base to amek new table in it and insert values in it"""
        self.window=window
        self.cur=cur
        self.con=con
        self.i=i
        self.second_page()
        self.radio_buttons()
    def radio_buttons(self):
        """This will creates two radio buttons both with two options for Grade and Division :)"""
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
        """First radio button working"""
        self.selected_value = self.selected_option.get()
        self.entrys9.delete(0, END)  # Clear the entry
        self.entrys9.insert(0, self.selected_value)  # Insert the selected value
    def on_radio_click1(self):
        """Second radio buttton working"""
        self.selected_value = self.selected_option.get()
        self.entrys10.delete(0, END)  # Clear the entry
        self.entrys10.insert(0, self.selected_value)
    def create_canvas(self):
        """Just creates a simple canvas along with logo"""
        self.canvas = Canvas(width=200, height=200)
        self.image1 = PhotoImage(file="logo2.png")
        self.canvas.create_image(100, 100, image=self.image1)
        self.canvas.grid(column=1, row=1,columnspan=3)
    def next_page(self):
        """THis will work if all the entries have some values,It will then isert that values into tthe table,DElete all the widgets created and create the method third page"""
        if self.data() :
            self.insert_data()
            for widget in self.window.winfo_children():#all the wigets inside that window get destroyed thorugh winfo_children() and destroy
                widget.destroy()
            self.create_canvas()
            self.third_page()
    def third_page(self):
        """THis will create an object from the class THIRD_PAGE"""
        self.third=Third_page(self.window,cur=self.cur,con=self.con,i=self.i)
    def data(self):
        """THis method will get data from all the entries and make attributes from them"""
        self.list2 = []
        self.list2.clear()
        self.Board=self.entrys1.get()
        self.degree_title=self.entrys2.get()
        self.exam_type=self.entrys3.get()
        self.passing_year=self.entrys4.get()
        self.roll_no=self.entrys5.get()
        self.regestration_no=self.entrys6.get()
        self.total_marks=self.entrys7.get()
        self.obtained_marks=self.entrys8.get()
        self.grade=self.entrys9.get()
        self.division=self.entrys10.get()
        self.list2+=self.Board,self.degree_title,self.exam_type,self.passing_year,self.roll_no,self.regestration_no,self.total_marks,self.obtained_marks,self.grade,self.division
        is_empty=False
        """This will return flase if ant of the entry is empty else true"""
        for i in self.list2:
             if i=="":
                 is_empty=True
        if is_empty:
            messagebox.showinfo(title="Data Error", message="Don't leave any field empty")
            return False
        return True
    def insert_data(self):
        """This method is used to create table if dosnot exoist and then insert data in the table DATA2"""
        try:
            self.cur.execute("CREATE TABLE DATA2 (id SERIAL PRIMARY KEY,BOARD TEXT,DEGREE TEXT,EXAM_TYPE TEXT,"
                             "PASSING_YEAR TEXT,ROLL_NO TEXT,REGESTRATION_NO TEXT,TOTAL_MARKS TEXT,OBTAINED_MARKS TEXT,GRADE TEXT,DIVISION TEXT)")
        except:
            self.add_data()
        else:
            self.add_data()
    def add_data(self):
        self.tupe = (self.i,self.Board,self.degree_title,self.exam_type,self.passing_year,self.roll_no,self.regestration_no,self.total_marks,self.obtained_marks,self.grade,self.division)
        self.cur.execute(f"INSERT INTO DATA2 VALUES {self.tupe}")
    def hsoe(self):
        """This is a private method just for checking the values when needed"""
        self.cur.execute(f"SELECT * FROM DATA2")
        r = self.cur.fetchall()
        for i1 in r:
            print()
            for j in i1:
                print(j)
    def second_page(self):
        """This method is used to create all the widgets forr the second page of the GUI"""
        self.label12=Label()
        # self.label12.grid(column=0, row=10, columnspan=5, padx=10)
        self.label12 = Label(text="(Matriculation!)")
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
