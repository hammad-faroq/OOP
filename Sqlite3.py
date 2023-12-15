import sqlite3
is_on=True
con = sqlite3.connect("def.db")
cur = con.cursor()
# cur.execute("CREATE TABLE DATA2(id SERIAL PRIMARY KEY,CODE TEXT,TITLE TEXT,CREDITS HOURS INT,SEMESTER INT,TYPE TEXT)")
i = 1
while is_on:
    user = input("Choose from these options:\na)Add s)Search d)Delete l)list all e)Edit q)Quit: ")
    if user=="a" or user=="s" or user=="d" or user=="l" or user=="e" or user=="q":
        if user=="a":
            user1 = input("Enter the code of the course: ").ljust(8)
            user2 = input("Enter the title of the course: ").ljust(40)
            user3 = int(input("Enter the creidt hours of the course: "))
            user4 = int(input("Enter the default semester of the course: "))
            user5 = input("Enter the type of the course type core or elective: ").ljust(8)
            data = (i, user1, user2, user3, user4, user5)
            # #WE have to write '' to insert the strings into the database
            cur.execute(f"INSERT INTO DATA2 VALUES {data}")
            con.commit()
            i+=1
        elif user=="s":
            record=input("Enter the record you want to search ,type id or CODE or TITLE or CREDITS HOURS or SEMESTER or TYPE: ")
            record_no=int(input("Enter the number of record type '0' if you dont want this method :"))
            cur.execute(f"SELECT {record} FROM DATA2")
            r = cur.fetchall()
            if record_no>0:
                print(r[record_no])
            else:
                for i1 in r:
                    for j in i1:
                        print(j)
        elif user=="d":
            record = input("Enter the record you want to delete ,type id or CODE or TITLE or CREDITS HOURS or SEMESTER or TYPE: ")
            record_no=(input("ENter the id or name of the record you want to delete :"))
            cur.execute(f"DELETE FROM DATA2 where {record}={record_no}")
            con.commit()
            print(f"DELETED SUccessfully from that {record}")
        elif user=="q":
            con.close()
            is_on=False
        elif user=="l":
            cur.execute(f"SELECT * FROM DATA2")
            r = cur.fetchall()
            for i1 in r:
                print()
                for j in i1:
                    print(str(j).strip(),end=" ")
            print()
        elif user=="e":
            record1 = str(input("Enter the record you want to edit ,type id or CODE or TITLE or CREDITS HOURS or SEMESTER or TYPE: "))
            record_previous =str(input("Enter the previous record you want to change :"))
            record_changed = str(input("Enter the new record :"))
            cur.execute(f"UPDATE DATA2 SET {record1} = {record_changed} WHERE {record1} = {record_previous}")
            con.commit()
            print("Updated successfully")
    else:
        user = input("Invalid input choose from these options:\n a)Add s)Search d)Delete l)list all e)Edit q)Quit: ")





























# all_data=f"{user1}{user2}{user3}{user4}{user5}"
# con=sqlite3.connect("abc.db")
# cur=con.cursor()
# # cur.execute("CREATE TABLE abc(ID INT,name CHAR[40],gender CHAR[5]")
# # cur.execute("INSERT INTO abc(ID,name,gender) VALUES(1,hammad,male)")
# # cur.execute("Create table student (ID INT,code CHAR[8],title CHAR[40],credits hours INT,default semester INT,type CHAR[8])")
# cur.execute("INSERT INTO student (ID,code,title,credits hours,default semester,type) VALUES (1,OOp,OBJECT ORIENTED PROG,4,2,CORE)")
# # con.commit()
# format="8s 40s i i 8s"
# format1="8s 40s i i 8s"
# with open(file="data.txt",mode="rb") as file:
#     # if user=="a":
#     #     data=input("Enter the data you want to enter as a list:")
#     #     i1=data[0].ljust()
#     # data1=struct.pack(format,user1.encode(),user2.encode(),user3,user4,user5.encode())
#     # file.write(data1)
#     data1=file.readline()
#     print(data1)
#     b=struct.unpack(format,data1)
#     print(b[0].decode())
#     print(b[1].decode())
#     print(b[2])
#     print(b[3])
#     print(b[4].decode())


