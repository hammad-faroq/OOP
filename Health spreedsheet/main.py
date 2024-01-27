import requests
from datetime import datetime
import os
from tkinter import*
def get_data():
    API_ENDPOINT="https://trackapi.nutritionix.com/v2/natural/exercise"
    os.environ["API_ENDPOINT"]=API_ENDPOINT
    API=os.getenv("API_ENDPOINT")
    API_KEY="43bb751073740bc54a4b7edffc3c8690"
    ID="b2803e78"
    os.environ["API_key"]=API_KEY
    os.environ["API_ID"]=ID
    API_ID=os.getenv("API_ID")
    API_KEY=os.getenv("API_KEY")
    header={
        "x-app-id":API_ID,
        "x-app-key":API_KEY
    }
    new_data=str(data1.get())
    user_dict={
     "query":new_data,
     "gender":"male",
     "weight_kg":61.5,
     "height_cm":174.64,
     "age":20
    }
    response=requests.post(url=API_ENDPOINT, json=user_dict, headers=header)
    response.raise_for_status()
    data=response.json()
    exercise=data['exercises']
    URL="https://api.sheety.co/b825cfaec200ae63cfe3cde3902a127e/copyOfMyWorkouts/workouts"
    time=datetime.now()
    formatted_time=time.strftime("%d/%m/%Y")
    formatted_hour=time.strftime("%H:%M:%S")
    for key in exercise:
        print("YEs")
        text={
          "workout":{
              "date": formatted_time,
              "time": formatted_hour,
              "exercise": key["user_input"],
              "duration": key["duration_min"],
              "calories": key["nf_calories"],
            }
        }
    #basic Authorization
    header={
    "Authorization": "Basic aGFtbWFkOkhhbW1hRHB1Y2l0MDEyMw=="
    }
    response=requests.post(URL, json= text, headers=header)
    button.config(state="disabled")
window=Tk()
window.title("Health :)")
window.config(width=200,height=200,padx=30,pady=30)
label=Label()
label.config(text="You Exercise")
label.grid(column=0,row=0)
data1=Entry()
data1.grid(column=1,row=0)
button=Button()
d=button.config(text="Insert",width=10,pady=5,command=get_data)
button.grid(column=1,row=1)

window.mainloop()