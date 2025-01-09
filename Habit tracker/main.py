import requests
from datetime import datetime
from tkinter import*
PIXELA_ENDPIONT="https://pixe.la/v1/users"
TOKEN="pythonpucit"
USER_NAME="hammeedfarooq"
# user_dict={
#     "token":"pythonpucit",
#     "username":"hammeedfarooq",
#     "agreeTermsOfService":"yes",
#     "notMinor":"yes"
# }
# response=requests.post(url=PIXELA_ENDPIONT,json=user_dict)##This is a method to create an account using HTTP method(with requests)
# print(response.text)
def get_data():
    new_data=str(data.get())
    date = datetime.now()
    FORMATTED_DATE = (date.strftime("%Y%m%d"))

    ID = "graph"
    ADDING_VALUE_ENDPOINT = f"{PIXELA_ENDPIONT}/{USER_NAME}/graphs/{ID}"
    data_dict3 = {
        "date": date.strftime("%Y%m%d"),
        "quantity":new_data ,
    }
    header = {
        "X-USER-TOKEN": TOKEN
    }
    print(type(new_data))
    response=requests.post(url=ADDING_VALUE_ENDPOINT, json=data_dict3, headers=header)
    print(response.text)
    button.config(state="disabled")
window=Tk()
window.title("Coding :)")
window.config(width=200,height=200,padx=30,pady=30)
label=Label()
label.config(text="You work")
label.grid(column=0,row=0)
data=Entry()
data.grid(column=1,row=0)
button=Button()
d=button.config(text="Insert",width=10,pady=5,command=get_data)
button.grid(column=1,row=1)


GRAPH_ENDPIONT=f"{PIXELA_ENDPIONT}/{USER_NAME}/graphs"

# user_dict2={
#     "id":"graph",
#     "name":"running",
#     "unit":"hr",
#     "type":"int",
#     "color":"ajisai"
# }


# response=requests.post(url=GRAPH_ENDPIONT, json=user_dict2, headers=header)
# print(response.text)

window.mainloop()


#update if you have post worng info
# UPDATE_ENDPOINT=f"{PIXELA_ENDPIONT}/{USER_NAME}/graphs/{ID}/{FORMATTED_DATE}"
#
# data_dict4={
#     "quantity":"1"
# }
# response=requests.put(url=UPDATE_ENDPOINT, json=data_dict4, headers=header)
# print(response.text)
#to delete a pixel
# response=requests.delete(url=UPDATE_ENDPOINT, headers=header)
# print(response.text)