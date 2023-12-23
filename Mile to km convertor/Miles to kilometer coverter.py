from tkinter import*
def convertor():
    miles_data=float(input.get())
    km_converted=round((miles_data * 1.609344),5)
    lebel2["text"]=km_converted


window=Tk()
window.title("Mile to Km converter")
window.minsize(width=200,height=150)
window.config(padx=7,pady=30)
#Entery
input=Entry(width=10)
input.grid(column=2,row=1)
#label 1
label=Label()
label["text"]="is equal to"
label.grid(column=1,row=2)
# label.config(padx=15,pady=50)

lebel2=Label()
lebel2["text"]="0"
lebel2.grid(column=2,row=2)

label3=Label()
label3.config(text="Miles")
label3.grid(column=3,row=1)

label3=Label()
label3.config(text="Km")
label3.grid(column=3,row=2)

#button
button=Button(text="Calculate",command=convertor)
button.grid(column=2,row=3)















window.mainloop()