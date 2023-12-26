import tkinter
from tkinter import*
class Last_page:
    def __init__(self,cur,con,window):
        self.window=window
        self.con=con
        self.cur=cur
        self.last()
        self.button()
    def last(self):
        """This method will create labels for the last page"""
        FONT_NAME = "Courier"
        self.labels01 = Label()
        self.labels01.config(text="")
        self.labels01.grid(column=0, row=2, pady=10)
        self.labels1 = Label()
        self.labels1.config(text="The End Do You want to Proceed! :")
        self.labels1.config(font = (FONT_NAME, 15, "bold"))
        self.labels1.grid(column=1, row=2,columnspan=2, pady=10)
    def button(self):
        """this method will create buttons for the last page"""
        self.button1 = Button()
        self.button1.config(text="Proceed!", width=33, command=self.next_page)
        self.button1.grid(column=1, row=3, pady=10)
        self.label18 = Label()
        self.label18.config(text="")
        self.label18.grid(column=0, row=3)
    def next_page(self):
        """This is the working for the button PRoceed"""
        FONT_NAME = "Courier"
        self.labels01 = Label()
        self.labels01.config(text="")
        self.labels01.grid(column=0, row=4, pady=10)
        self.labels1 = Label()
        self.labels1.config(text="Thanks :)")
        self.labels1.config(font=(FONT_NAME, 20, "bold"))
        self.labels1.grid(column=1, row=4, columnspan=2, pady=10)
        self.button01=Button()
        self.button01.config(text="Show Data!",width=33,command=self.merit)
        self.button01.grid(column=0,row=5,columnspan=2)

    def data(self):
        """This is behind the ceen working of the button sHow.We pressed it will fetch data from all the tables and then creates new labesl in a loop to show the data """
        self.button01.config(state=tkinter.DISABLED)
        self.record_no = self.entry101.get()
        self.upto = self.entry01.get()
        record_upto = int(self.upto)
        record_no = int(self.record_no)
        for i in range(record_no, record_upto + 1):
            self.cur.execute(f"SELECT * FROM DATA WHERE id = ?", (i,))
            self.j = self.cur.fetchall()
            try:
                self.r = self.j[0]
            except IndexError:
                pass
            else:
                self.name = self.r[1]
                self.f_Name = self.r[3]
                label = Label()
                label.config(text=f"Name :{self.name}{self.f_Name}")
                label.pack()
                self.cur.execute(f"SELECT * FROM DATA2 WHERE id = ?", (i,))
                self.j = self.cur.fetchall()
                self.r = self.j[0]
                self.board = self.r[1]
                self.which = self.r[2]
                self.total = int(self.r[7])
                self.obt = int(self.r[8])
                self.per = round((self.obt / self.total) * 100, 2)
                label1 = Label()
                label1.config(text=f"Board :{self.board}\tClass :{self.which}\tpercentage{self.per}")
                label1.pack()
                self.cur.execute(f"SELECT * FROM DATA3 WHERE id = ?", (i,))
                self.j = self.cur.fetchall()
                self.r = self.j[0]
                self.board1 = self.r[1]
                self.which1 = self.r[2]
                self.total1 = int(self.r[7])
                self.obt1 = int(self.r[8])
                self.per1 = round((self.obt1 / self.total1) * 100, 2)
                label2 = Label()
                label2.config(text=f"Board :{self.board1}\tClass :{self.which1}\tpercentage{self.per1}")
                label2.pack()
                label3 = Label()
                label3.config(text="______________________________________________________________________")
                label3.pack()
    def merit(self):
        """This is the working of the button SHow Data!.It Clears the previous screen.And ask for two inputs for the range of applicants.It also has a button (Show)"""
        for widget in self.window.winfo_children():  # all the wigets inside that window get destroyed thorugh winfo_children() and destroy
            widget.destroy()
        self.label101 = Label()
        self.label101.config(text="Enter THe Start of the Students from number ::")
        self.label101.pack()
        self.entry101 = Entry(width=20)
        self.entry101.pack()
        self.label01 = Label()
        self.label01.config(text="Enter the Last number you want upto :")
        self.label01.pack()
        self.entry01 = Entry(width=20)
        self.entry01.pack()
        self.button01 = Button()
        self.button01.config(text="show", command=self.data)
        self.button01.pack()