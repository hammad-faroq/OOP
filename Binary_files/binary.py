import struct
import student,grades
with open(file="record.txt",mode="r") as file:
    data=file.readline()
    b1=int(data)
course2=""
def func(roll,semes,name,e):
    """This function is to print the student data"""
    depart=g[2]
    phone1=g[3]
    marks = round(e[2], 1)
    course1=course()
    percentage=round(e[3],2)
    g.clear()
    return (f"NAme:{name} ROll_no: {roll}\nDepartment_code: {depart} Phone_no"
            f": {phone1}\nSemester :"
            f"{semes} Last_semester_marks :{marks}\nPercentage{percentage} Course :{course1}")
def course():
    """This function is to select the course from the list"""
    global  course2
    course2=""
    try:
        course2 = g[4] + " " + g[5]
    except:
        course2 = g[4]
    else:
        try:
            course2 = g[4] + " " + g[5] + " " + g[6]
        except:
            course2 = g[4] + " " + g[5]
        else:
            pass
    return course2
def percentage_calculator(percentage):
    """This function is to calculate the percenrage with grade"""
    if 3.7 <= percentage >= 4:
        percentage = str(percentage) + "  A"
    elif 3.3 <= percentage >= 3.69:
        percentage = str(percentage) + "  A+"
    elif 3 <= percentage >= 3.29:
        percentage = str(percentage) + "  B"
    elif 2.7 <= percentage >= 2.99:
        percentage = str(percentage) + "  B+"
    elif 2.3 <= percentage >= 2.69:
        percentage = str(percentage) + "  B-"
    elif 2.3 <= percentage >= 2.69:
        percentage = str(percentage) + "  B-"
    elif 2 <= percentage >= 2.29:
        percentage = str(percentage) + "  C+"
    elif 1.7 <= percentage >= 1.99:
        percentage = str(percentage) + "  C"
    elif 1.3 <= percentage >= 1.69:
        percentage = str(percentage) + "  C-"
    else:
        percentage = str(percentage) + "  F"
    return percentage
def one_by_one (datat,which):
    """This function is used to print the transcript and summary sheet,award sheet"""
    with open(file="data.txt",mode="rb+") as file:
        g2 = []
        for i in range(b1):
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
            semes = e2[1]
            na = f"{g2[0]}{g2[1]}"
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
            percentage = round(e2[3], 2)
            g2.clear()
            if course == datat:
                if which=="summary":
                    print()
                    print(
                    f"Name:{na} ROll_no: {roll}\nCourse :{course}")
                elif which=="trans":
                    print()
                    print(
                        f"NAme:{na} ROll_no: {roll} Semester :{semes}\nPercentage{percentage} Course :{course}")
def insert (datat1):
    """This function is used to insert data into the binary file """
    nam = input("Enter the full_name of the student :")
    dap = input("Enter the department Code of the student :")
    sem = int(input("enter the semester of the student :"))
    last_marks = float(input("Enter the last_semester marks of the student :"))
    p_no = input("Enter the phone nuber of the student :")
    cour = input("Enter the course of the student :")
    p_m = float(input("enter the percentage marks of the student :"))
    s1 = student.Student(roll_no=datat1, name=nam, department=dap, semseter=sem, lasst_semseter_marks=last_marks,
                         ph_no=p_no)
    s2 = grades.Grades(course=cour, roll_no=datat1, percentage_marks=p_m)
    fo1 = "79s i f f"
    with open(file="data.txt", mode="ab+") as file1:
        data = f"{s1.roll_no}{s1.name}{s1.department_code}{s1.phone_no}{s2.course}"
        bytes1 = struct.Struct(fo1)
        v = bytes1.pack(data.encode("utf-8"), s1.semester, s1.last_semester_marks, s2.percentage_marks)
        file1.write(v)
while True:
    print("\n")
    user = int(input(
        "Enter the operation you want to do:"
        "\n1) QUIT the management system 2)Add a Student \n3)view a student by roll_no 4) Edit student by roll no\n5) Delete student by roll no 6) List student by semester"
        "\n7) List students by name 8) Print students list\n14) List Student wise (1 student) grade of courses 15. List Course wise grade (1 course) of students\n"
        "16) Award sheet 17) Summary sheet\n18) Transcripts for a range of students\n\n"))
    # user=int(input("Enter :"))
#1. QUIT the management system
    if user==1:
        break
    # 2. Add a student (check for NO duplicates)
    elif user==2:
        def roll_no_check():
            global  r
            datat=input("Enter the roll_no of the student :").lower()
            fo1="79s i f f"
            with open(file="data.txt",mode="rb+") as file1:
                n="roll no"
                for i in range(b1):
                    f=file1.readline(92)
                    try:
                        c=struct.unpack(fo1,f)
                    except:
                        insert(datat1=datat)
                    else:
                        d = c[0].decode("utf-8")
                        roll_no = d.split(" ")[0]
                        if datat in roll_no:
                            n="same roll no"
                            return  n
                with open(file="record.txt", mode="r+") as file:
                    data1 = file.read()
                    # print(data1)
                    j=int(data1)
                    j+=1
                    r=str(j)
                    file.seek(0)
                    file.write("")
                    file.seek(0)
                    file.write(r)
                insert(datat)
                return n
        print(roll_no_check())

    #3. View student by roll no
    elif user==3:
        with open(file="data.txt",mode="rb") as file:
            datat = input(f"Enter the roll_no of the student :")
            g=[]
            for i in range(b1):
                c=file.readline(92)
                fo1="79s i f f"
                e=struct.unpack(fo1,c)
                f = e[0].decode("utf-8").split(" ")
                roll=f[0]
                if roll == datat:
                    for i in f[1:]:
                        if i=="":
                            pass
                        else:
                            g.append(i)
                    semes = e[1]
                    na = f"{g[0]}{g[1]}"
                    print(func(roll,semes,na,e))
    #5. Delete student by roll no
    elif user == 5:
        k=0
        with open(file="delete.txt",mode="rb+") as file:
            datat = input(f"Enter the roll_no of the student you want to delete :")
            g = []
            for i in range(b1):
                c = file.readline(92)
                fo1 = "79s i f f"
                e = struct.unpack(fo1, c)
                f = e[0].decode("utf-8").split(" ")
                roll = f[0]
                if roll == datat:
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
    #4. Edit student by roll no (check for NO duplicates)
    elif user == 4:
        k=0
        with open(file="delete.txt",mode="rb+") as file:
            datat = input(f"Enter the roll_no of the student you want to edit :")
            g3 = []
            for i in range(b1):
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
                        # print("yes")
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

    #6. List student by semester
    elif user==6:
        with open(file="data.txt",mode="rb") as file:
            datat = int(input(f"Enter the semester of the student :"))
            for i in range(b1):
                c=file.readline(92)
                fo1="79s i f f"
                e=struct.unpack(fo1,c)
                f = e[0].decode("utf-8").split(" ")
                g=[]
                for i in f[1:]:
                    if i == "":
                        pass
                    else:
                        g.append(i)
                semes = e[1]
                if semes == datat:
                    na = f"{g[0]}{g[1]}"
                    roll = f[0]
                    print(func(roll, semes, na, e))
    #7. List students by name
    elif user==7:
        with open(file="data.txt",mode="rb") as file:
            datat = input(f"Enter the name of the student :")
            for i in range(b1):
                c=file.readline(92)
                fo1="79s i f f"
                e=struct.unpack(fo1,c)
                g=[]
                f = e[0].decode("utf-8").split(" ")
                for i in f[1:]:
                    if i == "":
                        pass
                    else:
                        g.append(i)
                na = f"{g[0]}"
                if na == datat:
                    roll = f[0]
                    semes = e[1]
                    print(func(roll, semes, na, e))
                na = f"{g[0]}{g[1]}"
                if na == datat:
                    roll = f[0]
                    semes = e[1]
                    print(func(roll, semes, na, e))

    #8. Print students list
    elif user==8:
        with open(file="data.txt",mode="rb") as file:
            g2 = []
            for i in range(b1):
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
                semes = e2[1]
                na = f"{g2[0]}{g2[1]}"
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
                print (f"NAme:{na} ROll_no: {roll}\nDepartment_code: {depart} Phone_no: {phone1}\nSemester :{semes} Last_semester_marks :{marks}\nPercentage{percentage} Course :{course}")
                print()
                g2.clear()
    #14. List Student wise (1 student) grade of courses
    if user==14:
        with open(file="data.txt",mode="rb") as file:
            datat = input("Enter the Name of the student :")
            g = []
            for i in range(b1):
                c = file.readline(92)
                fo1 = "79s i f f"
                e = struct.unpack(fo1, c)
                f = e[0].decode("utf-8").split(" ")
                for i in f[1:]:
                    if i == "":
                        pass
                    else:
                        g.append(i)
                na1 = f"{g[0]}{g[1]}"
                marks = round(e[2], 2)
                if na1 == datat:
                    roll = f[0]
                    semes = e[1]
                    course1=course()
                    percentage1=percentage_calculator(marks)
                    print(f"NAme:{na1} ROll_no: {roll}\nSemester :{semes} Percentage :{percentage1}\nCourse :{course1}")
                g.clear()
    #15. List Course wise grade (1 course) of students
    elif user==15:
        with open(file="data.txt",mode="rb") as file:
            datat = input("Enter the course you want to check :")
        one_by_one(datat)
    # 16. Award sheet (courses one by one, with students enrolled in it)
    elif user==16:
        h6=[]
        course_data=[""]
        with open(file="data.txt",mode="rb") as file:
            for i in range(b1):
                c5=file.readline(92)
                fo1 = "79s i f f"
                e4 = struct.unpack(fo1, c5)
                f4 = e4[0].decode("utf-8").split(" ")
                for i in f4[1:]:
                    if i == "":
                        pass
                    else:
                        h6.append(i)
                try:
                    course1 = h6[4] + " " + h6[5]
                except:
                    course1 = h6[4]
                else:
                    try:
                        course1 = h6[4] + " " + h6[5] + " " + h6[6]
                    except:
                        course1 = h6[4] + " " + h6[5]
                    else:
                        pass
                if course1 not in course_data:
                    h6.clear()
                    print("_______________________Award sheet____________________________")
                    one_by_one(datat=course1,which="summary")
                    print("___________________________________________________")
                    # print(course1)
                    course_data.append(course1)
                else:
                    h6.clear()
                    continue
    #17. Summary sheet (courses info, one by one, with one line for each student in it)
    elif user==17:
        print("________________________________summary sheet____________________________________")
        h6 = []
        course_data = [""]
        with open(file="data.txt", mode="rb") as file:
            for i in range(b1):
                c5 = file.readline(92)
                fo1 = "79s i f f"
                e4 = struct.unpack(fo1, c5)
                f4 = e4[0].decode("utf-8").split(" ")
                for i in f4[1:]:
                    if i == "":
                        pass
                    else:
                        h6.append(i)
                try:
                    course1 = h6[4] + " " + h6[5]
                except:
                    course1 = h6[4]
                else:
                    try:
                        course1 = h6[4] + " " + h6[5] + " " + h6[6]
                    except:
                        course1 = h6[4] + " " + h6[5]
                    else:
                        pass
                if course1 not in course_data:
                    h6.clear()
                    one_by_one(datat=course1,which="trans")
                    print("___________________________________________________")
                    course_data.append(course1)
                else:
                    h6.clear()
                    continue
    #18. Transcripts for a range of students
    elif user==18:
        us=int(input("Enter the start range of roll numbers to any number :"))
        us1 = int(input("Enter the end range of roll numbers :"))
        d=input("Enter the department :")
        print("________________________________TRANSCRIPT____________________________________")
        with open(file="data.txt", mode="rb") as file:
            course1 = ""
            m3=[]
            for i in range(us,us1+1):
                roll1=d+str(i)
                file.seek(0)
                for i in range(b1):
                    c3 = file.readline(92)
                    fo1 = "79s i f f"
                    e3 = struct.unpack(fo1, c3)
                    f3 = e3[0].decode("utf-8").split(" ")
                    roll = f3[0]
                    for i in f3[1:]:
                        if i == "":
                            pass
                        else:
                            m3.append(i)
                    na = f"{m3[0]}{m3[1]}"
                    course1 = ""
                    try:
                        course1 = m3[4] + " " + m3[5]
                    except:
                        course1 = m3[4]
                    else:
                        try:
                            course1 = m3[4] + " " + m3[5] + " " + m3[6]
                        except:
                            course1 = m3[4] + " " + m3[5]
                        else:
                            pass
                    marks = round(e3[2], 2)
                    per1 = percentage_calculator(marks)
                    depart = m3[2]
                    phone1 = m3[3]
                    semes = str(e3[1])
                    m3.clear()
                    if roll1 == roll:
                        m3.clear()
                        print(f"NAme:{na} ROll_no: {roll}\nDepartment_code: {depart} "
                              f"Phone_no: {phone1}\nSemester :{semes} Last_semester_marks :{marks}\nPercentage{per1} Course :{course1}")
                        print()
                        print("___________________________________________________")
"""Credits:Hammad Farooq ,
department:Data science,
Roll_no: bsdsf22a026,
University : PUCIT"""