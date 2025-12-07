import struct
import student,grades
# user =int(input("Enter"))
course2=""
j=2
while True:
    user = int(input("Enter"))
    if user==1:
        with open(file="delete.txt",mode="ab+") as file:
            datat = input("Enter the roll_no of the student :").lower()
            fo1 = "79s i f f"
            f = file.read()
            try:
                c = struct.unpack(fo1, f)
            except:
                nam = input("Enter the name of the student :")
                dap = input("Enter the department Code of the student :")
                sem = int(input("enter the semester of the student :"))
                last_marks = float(input("Enter the last_semester marks of the student :"))
                p_no = input("Enter the phone nuber of the student :")
                cour = input("Enter the course of the student :")
                p_m = float(input("enter the percentage marks of the student :"))
            else:
                d = c[0].decode("utf-8")
                roll_no = d.split(" ")[0]
                print(roll_no)
                if datat in roll_no:
                    print("same roll no")
                else:
                    nam = input("Enter the full_name of the student :")
                    dap = input("Enter the department Code of the student :")
                    sem = int(input("enter the semester of the student :"))
                    last_marks = float(input("Enter the last_semester marks of the student :"))
                    p_no = input("Enter the phone nuber of the student :")
                    cour = input("Enter the course of the student :")
                    p_m = float(input("enter the percentage marks of the student :"))
            finally:
                s1 = student.Student(roll_no=datat, name=nam, department=dap, semseter=sem, lasst_semseter_marks=last_marks,
                                         ph_no=p_no)
                s2 = grades.Grades(course=cour, roll_no=datat, percentage_marks=p_m)
                fo1 = "79s i f f"
                data = f"{s1.roll_no}{s1.name}{s1.department_code}{s1.phone_no}{s2.course}"
                bytes1 = struct.Struct(fo1)
                v = bytes1.pack(data.encode("utf-8"), s1.semester, s1.last_semester_marks, s2.percentage_marks)
                file.write(v)
    elif user == 6:
        k=0
        with open(file="delete.txt",mode="rb+") as file:
            datat = input(f"Enter the roll_no of the student you want to delete :")
            g = []
            for i in range(j):
                c = file.readline(92)
                # print(c)
                fo1 = "79s i f f"
                e = struct.unpack(fo1, c)
                f = e[0].decode("utf-8").split(" ")
                roll = f[0]
                if roll == datat:
                    # print("yes")
                    s1 = student.Student(roll_no='', name="", department='', semseter=0,
                                             lasst_semseter_marks=0.0,
                                             ph_no='')
                    s2 = grades.Grades(course="", roll_no="", percentage_marks=0.0)
                    fo1 = "79s i f f"
                    data = f"{s1.roll_no}{s1.name}{s1.department_code}{s1.phone_no}{s2.course}"
                    bytes1 = struct.Struct(fo1)
                    v = bytes1.pack(data.encode("utf-8"), s1.semester, s1.last_semester_marks, s2.percentage_marks)
                    file.seek(k)
                    file.write(v)
                    break
                else:
                    k+=92
    elif user == 7:
        k=0
        with open(file="delete.txt",mode="rb+") as file:
            datat = input(f"Enter the roll_no of the student you want to edit :")
            g3 = []
            for i in range(j):
                c = file.readline(92)
                fo1 = "79s i f f"
                e2 = struct.unpack(fo1, c)
                f3 = e2[0].decode("utf-8").split(" ")
                roll = f3[0]
                for i in f3[1:]:
                    if i == "":
                        pass
                    else:
                        g3.append(i)
                semes = e2[1]
                try:
                    na = f"{g3[0]} {g3[1]}"
                except:
                    pass
                else:
                    course = ""
                    try:
                        course = g3[4] + " " + g3[5]
                    except:
                        course = g3[4]
                    else:
                        try:
                            course = g3[4] + " " + g3[5] + " " + g3[6]
                        except:
                            course = g3[4] + " " + g3[5]
                        else:
                            pass
                    depart = g3[2]
                    phone1 = g3[3]
                    marks = round(e2[2], 1)
                    percentage = round(e2[3], 2)
                if roll == datat:
                    print("yes")
                    datat = input(f"Enter the new roll_no of the student :")
                    s1 = student.Student(roll_no=datat, name=na, department=depart, semseter=semes,lasst_semseter_marks=marks,
                                             ph_no=phone1)
                    s2 = grades.Grades(course=course, roll_no=datat, percentage_marks=percentage)
                    fo1 = "79s i f f"
                    data = f"{s1.roll_no}{s1.name}{s1.department_code}{s1.phone_no}{s2.course}"
                    bytes1 = struct.Struct(fo1)
                    v = bytes1.pack(data.encode("utf-8"), s1.semester, s1.last_semester_marks, s2.percentage_marks)
                    file.seek(k)
                    file.write(v)
                    break
                else:
                    k+=92
    elif user == 8:
        with open(file="delete.txt", mode="rb") as file:
            g2 = []
            for i in range(j):
                c1 = file.readline(92)
                fo1 = "79s i f f"
                e2 = struct.unpack(fo1, c1)
                f2 = e2[0].decode("utf-8").split(" ")
                roll = f2[0]
                for i in f2[1:]:
                    if i == "":
                        pass
                    else:
                        g2.append(i)
                # print(g2)
                semes = e2[1]
                try:
                    na = f"{g2[0]}{g2[1]}"
                except:
                    pass
                else:
                    course = ""
                    try:
                        course = g2[4] + " " + g2[5]
                    except:
                        course = g2[4]
                    else:
                        try:
                            course = g2[4] + " " + g2[5] + " " + g2[6]
                        except:
                            course = g2[4] + " " + g2[5]
                        else:
                            pass
                    depart = g2[2]
                    phone1 = g2[3]
                    marks = round(e2[2], 1)
                    percentage = round(e2[3], 2)
                    print(f"NAme:{na} ROll_no: {roll}\nDepartment_code: {depart} Phone_no: {phone1}\nSemester :{semes} Last_semester_marks :{marks}\nPercentage{percentage} Course :{course}")
                    print()
                    g2.clear()





















                    # for i in f[1:]:
                    #     if i == "":
                    #         pass
                    #     else:
                    #         g.append(i)
                    # semes = e[1]
                    # na = f"{g[0]}{g[1]}"
                    # course2 = ""
                    # try:
                    #     course2 = g[3] + " " + g[4]
                    # except:
                    #     course2 = g[3]
                    # else:
                    #     try:
                    #         course2 = g[3] + " " + g[4] + " " + g[5]
                    #     except:
                    #         course2 = g[3] + " " + g[4]
                    #     else:
                    #         pass
                    # depart = g[1]
                    # phone1 = g[2]
                    # marks = round(e[2], 1)
                    # percentage = round(e[3], 2)
                    # g.clear()
                    # print (f"NAme:{na} ROll_no: {roll}\nDepartment_code: {depart} Phone_no"
                    #         f": {phone1}\nSemester :"
                    #         f"{semes} Last_semester_marks :{marks}\nPercentage{percentage} Course :{course1}")