import random

BACKGROUND_COLOR = "#B1DDC6"
from tkinter import*
import pandas
from random import choice

#___________________________________________pandas__________________________________________
try:
    df=pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    df=pandas.read_csv("french_words.csv")
finally:
    nested_dict=df.to_dict(orient="records")
    slected_dict={}
    updated_dict={}

def word_generator():
    global slected_dict,flip_timer
    window.after_cancel(flip_timer)#this method stops the timer,and then satrts again duwe to last statement
    slected_dict=choice(nested_dict)
    french_word=(slected_dict["French"])
    english_word=(slected_dict["English"])#if we want to update our text store it into a variable and then use canvas.itemconfig(var,new_text)
    canvas.itemconfig(card_flip,image=image1)
    canvas.itemconfig(title,text="French",fill="black")
    canvas.itemconfig(word,text=french_word,fill="black")
    flip_timer = window.after(3000, func=flip_card)#this method starts the timemr again
def flip_card():
    global slected_dict
    canvas.itemconfig(card_flip,image=image2)
    canvas.itemconfig(title,text="Engish",fill="white")
    canvas.itemconfig(word,text=slected_dict["English"],fill="white")

def remove_word():
    global updated_dict
    print(slected_dict)
    try:
        nested_dict.remove(slected_dict)
    except ValueError:
        print("dont press the button two times")
    else:
        updated_dict=nested_dict
    finally:
        print(updated_dict)
        df=pandas.DataFrame(updated_dict)
        df.to_csv("words_to_learn.csv",index=False)
        word_generator()





#____________________________________________________________________________________________
window=Tk()
window.title("flashy")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
flip_timer=window.after(3000,func=flip_card)

canvas=Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
image1=PhotoImage(file="images/card_front.png")
image2=PhotoImage(file="images/card_back.png")
card_flip=canvas.create_image(400,263,image=image1)
canvas.grid(column=0,row=0,columnspan=2)
#text1
title=canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
canvas.grid(column=0,row=1)
#text2
word=canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=2)

#button1
button1=Button()
my_image=PhotoImage(file="images/wrong.png")
button1.config(image=my_image,highlightthickness=0,command=word_generator)
button1.grid(column=0,row=3)
#button2
button=Button()
my_image1=PhotoImage(file="images/right.png")
button.config(image=my_image1,highlightthickness=0,bg=BACKGROUND_COLOR,command=remove_word)
button.grid(column=1,row=3)
word_generator()







window.mainloop()
