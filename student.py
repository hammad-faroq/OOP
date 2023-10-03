class Student():
    def __init__(self,name,age,gender,department,semester,course_list=[],course_percentage=[]):##deafult paramerers to catch the errors
        self.name=name
        self.age=age
        self.gender=gender
        self.department=department
        self.semester=semester
        self.course_list=course_list
        self.course_percentage=course_percentage
    @property
    def gender(self):
        return self._gender
    @gender.setter
    def gender(self,value):
        if value=="male" or value=="female":
            self._gender=value
        else:
            self.gender=input("Invalid gender enter again :")
    @property
    def semester(self):
        """Getter of the semester attribute(data member)"""
        return self._semester
    @semester.setter
    def semester(self,value):
        """Setter of the semester attribute"""
        if type(value)==int:
            if value<9 and value>0:
                self._semester=value
        else:
            self.semester=int(input("Invalid input enter the semester again: "))

    def update_semseter(self,value):
        """It will ust call the setter to update the semester's valid value"""
        self.semester=value
    def update_course_list(self,value):
        """It gets a tuple as a parameter in whiCh first value is the value you want to change
        ,next value is the replacement of the previous value and last one is the marks.It appends that course to the last of the list :)"""
        previous=value[0]
        change=value[1]
        marks=value[2]
        j=0
        previous_marks=0
        for i in self.course_list:
            if i==previous:
                self.course_list.remove(previous)
                self.course_list.append(change)
                previous_marks=self.course_percentage[j]
            j+=1
        for i in self.course_percentage:
            if i== previous_marks:
                self.course_percentage.remove(previous_marks)
                self.course_percentage.append(marks)
    def add_course(self,value):
        """It just adds new course to the previous list of courses and marks"""
        self.course_list.append(value[0])
        self.course_percentage.append(value[1])
    def total_percentage(self):
        """It gives us the total percentage of the total number of subjects"""
        j=0
        k=0
        for i in self.course_percentage:
            j+=int(i)
            k+=1
        k=str(k)
        k+="00"
        k=int(k)
        percentage=(j/k)*100
        percentage=round(percentage)
        print(f"Total marks are {j} out of {k} % which are {percentage}")
    def __str__(self):
        """It will print the output in the rite format you want"""
        j=0
        data1=""
        for i in self.course_list:
            course=i
            marks=self.course_percentage[j]
            j+=1
            data1+=f"Course :{course}\nMarks :{marks}\n"
        data=f"Name: {self.name}\nDepartment: {self.department}\nSemester :{self.semester}\nGender :{self.gender}\n{data1}"
        return data



s=Student("hammad",19,"male","data science",2,["pf","Ict","English","Quran","Descrete structures"],[69,61,78,91,63])
# print(s.gender)
# print(s.semester)
# s.update_semseter(13)
# print(s.semester)
# print(s.course_list)
# s.update_course_list(value=("English","Urdu1","91"))
# print(s.course_list)
# print(s.course_percentage)
# s.update_course_list(value=("Urdu1","Urd","00"))
# print(s.course_list)
# print(s.course_percentage)
# s.add_course(value=("papkistan studies",78))
# print(s.course_list)
# print(s.course_percentage)
# s.total_percentage()
print(s)
s.update_semseter("hello")
s.add_course(value=("Islamiyat",102))
print(s)
s.total_percentage()




