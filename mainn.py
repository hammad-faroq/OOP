from tkinter import*
# def convertor():
#     miles_data=float(input.get())
#     km_converted=round((miles_data * 1.609344),5)
#     lebel2["text"]=km_converted

class Cgpa:
    def __init__(self):
        self.create_window()
        self.entries()

    def create_window(self):
        self.window = Tk()
        self.window.title("CGPA Calculator")
        self.window.minsize(width=400, height=300)
        self.window.config(padx=7, pady=7)
    def calc(self):
        c1=float(self.input.get())
        m1=int(self.input1.get())
        c2 = float(self.input2.get())
        m2 = int(self.input3.get())
        c3 = float(self.input4.get())
        m3 = int(self.input5.get())
        c4 = float(self.input6.get())
        m4 = int(self.input7.get())
        cre=c1+c2+c3+c4
        marks=m1+m2+m3+m4
        gpa=round((c1*m1+c2*m2+c3*m3+c4*m4)/cre,2)
        print(gpa)
        self.label1["text"]=str(gpa)+"%"
    def entries(self):
        #Entery and label 1
        self.input=Entry(width=10)
        self.input.grid(column=2,row=1)
        self.input.config(width=20)
        self.label=Label()
        self.label["text"]="Enter Credit hours OOP  :"
        self.label.grid(column=1,row=1)
        # self.label.config(padx=3,pady=3)
        self.input1 = Entry(width=10)
        self.input1.grid(column=2, row=2)
        self.input1.config(width=20)
        self.label = Label()
        self.label["text"] = "Enter %age marks OOP  :"
        self.label.grid(column=1, row=2)
        # Entry and label 2
        self.label = Label()
        self.label["text"] = "Enter Credit hours OOP_lab  :"
        self.label.grid(column=1, row=3)
        self.input2 = Entry(width=10)
        self.input2.grid(column=2, row=3)
        self.input2.config(width=20)
        self.label = Label()
        self.label["text"] = "Enter %age marks OOP_lab  :"
        self.label.grid(column=1, row=4)
        self.input3 = Entry(width=10)
        self.input3.grid(column=2, row=4)
        self.input3.config(width=20)
        # Entry and label 3
        self.label = Label()
        self.label["text"] = "Enter Credit hours English  :"
        self.label.grid(column=1, row=5)
        self.input4 = Entry(width=10)
        self.input4.grid(column=2, row=5)
        self.input4.config(width=20)
        self.label = Label()
        self.label["text"] = "Enter %age marks English  :"
        self.label.grid(column=1, row=6)
        self.input5 = Entry(width=10)
        self.input5.grid(column=2, row=6)
        self.input5.config(width=20)
        # Entry and label 4
        self.label = Label()
        self.label["text"] = "Enter Credit hours of IST  :"
        self.label.grid(column=1, row=7)
        self.input6 = Entry(width=10)
        self.input6.grid(column=2, row=7)
        self.input6.config(width=20)
        self.label = Label()
        self.label["text"] = "Enter %age marks of IST  :"
        self.label.grid(column=1, row=8)
        self.input7 = Entry(width=10)
        self.input7.grid(column=2, row=8)
        self.input7.config(width=20)
        self.label1=Label()
        self.label1["text"] = ""
        self.label1.grid(column=2,row=9)
        self.button=Button(text="calculate",command=self.calc)
        self.button.grid(column=2,row=10)
        self.window.mainloop()





c=Cgpa()










        # label 1
        # self.label = Label()
        # self.label["text"] = "Enter Credit hours OOP  :"
        # self.label.grid(column=1, row=1)
        # # Entery
        # self.input4 = Entry(width=10)
        # self.input4.grid(column=2, row=3)
        # self.input4.config(width=20)
        # # label 1
        # self.label = Label()
        # self.label["text"] = "Enter %age marks OOP  :"
        # self.label.grid(column=1, row=3)
    # label.config(padx=15,pady=50)

    # lebel2=Label()
    # lebel2["text"]="0"
    # lebel2.grid(column=2,row=2)
    #
    # label3=Label()
    # label3.config(text="Miles")
    # label3.grid(column=3,row=1)
    #
    # label3=Label()
    # label3.config(text="Km")
    # label3.grid(column=3,row=2)

    # #button
    # button=Button(text="Calculate",command=convertor)
    # button.grid(column=2,row=3)
c=Cgpa()