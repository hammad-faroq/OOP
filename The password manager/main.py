# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
from random import randint,choice,shuffle#to cut down the ... all tthe time
import pyperclip
import json
def password_generator():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters=[choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers=[choice(numbers) for char in range(randint(2, 4))]
    password_list=password_numbers+password_letters+password_symbols##it will alos join all the list into one single list
    shuffle(password_list)
    password="".join(password_list)#to convert a list in to string using join method
    entry3.delete(0,END)
    entry3.insert(0,string=password)
    # elif score==2:
    #     score=1
    #     entry3.delete(0,END)

    # score1+=1
    pyperclip.copy(text=password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
from tkinter import messagebox

def password_check():
    website_data = entry1.get()
    try:
        with open(file="data.json", mode="r") as data_file:
        # first read old data
            read = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="File Error",message="No Data File Found")
    else:
        if website_data in read:
            value=read[website_data]
            email=value["email"]
            password=value["password"]
            messagebox.showinfo(title="Your Data",message=f"Your email is :{email}\nYour password is :{password}")
            entry3.insert(0,password)
            print(email)
            print(password)
        else:
            messagebox.showinfo(title="No Data",message=f"No Details for the {website_data} exist")
def all_the_data():
    website_data=entry1.get()
    email_data=entry2.get()
    password_data=entry3.get()
    my_dictionary={
        website_data:
            {"email":email_data,
             "password":password_data}
    }
    # new_variable=website_data+" |"+email_data+" |"+password_data+"\n"
    if len(website_data)<1  or len(password_data)<1:
        messagebox.showerror(message="Please dont leave any of the fields empty")
    else:
        try: #if not exceed then EXCEPT ,if excedd then else
            with open(file="data.json",mode="r") as data_file:
                #first read old data
                read = json.load(data_file)
        except FileNotFoundError:
            with open(file="data.json", mode="w") as data_file:
                json.dump(my_dictionary,data_file,indent=4)

        else:
            #update the old data
            read.update(my_dictionary)
            with open(file="data.json",mode="w") as data_file1:
                #then write the old data
                json.dump(read,data_file1,indent=4  )
        finally: ##it goona triggered no matter waht happen
                entry1.delete(0,END)
                entry3.delete(0,END)
        # ---------------------------- UI SETUP ------------------------------- #
from tkinter import*
window=Tk()
window.title("Password manager")
window.config(padx=50,pady=50)
canvas=Canvas(width=200,height=200)
image1=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image1)
canvas.grid(column=1,row=1)
#Label1
label1=Label()
label1.config(text="Website:")
label1.grid(column=0,row=2)
#Label2
label2=Label()
label2.config(text="Email/User Name:")
label2.grid(column=0,row=3)

#label3
label3=Label()
label3.config(text="Password: ")
label3.grid(column=0,row=4)

#Entery label1
entry1=Entry(width=33)

data_website=entry1.get()
entry1.grid(column=1,row=2)


#Entery label2
entry2=Entry(width=52)
entry2.insert(0,"bsdsf22a026@pucit.edu.pk")
entry2.grid(column=1,row=3,columnspan=2)

#Entery label3
entry3=Entry(width=33)
entry3.grid(column=1,row=4)
#button genetate passowrd
button=Button(highlightthickness=0)
button.config(text="Generate password ",command=password_generator)
button.grid(column=2,row=4)

#button genetate passowrd
button=Button(width=44,command=all_the_data)
button.config(text="Add")
button.grid(column=1,row=5,columnspan=2)
#button search
button=Button(width=15,highlightthickness=0,command=password_check)
button.config(text="Search")
button.grid(column=2,row=2)





window.mainloop()