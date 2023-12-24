class Person(object):
    """This is the parent class"""
    def __init__(self,name,contact):
        self.name=name
        self.contact=contact
    def __str__(self):
        return f"Name: {self.name}\nContact: {self.contact}"
class Student(Person):
    """This is the child class1"""
    def __init__(self,name,contact,dep,sem):
        Person.__init__(self,name,contact)
        self.department=dep
        self.semester=sem
    def __str__(self):
        return f"Name:{self.name}\nContact: {self.contact}\nDepartment :{self.department}\nSemetser: {self.semester}"
class Teacher(Person):
    """This is the child class2"""
    def __init__(self,name,contact,course,office_no):
        Person.__init__(self,name,contact)
        self.course=course
        self.office_no=office_no
    def __str__(self):
        return f"Name: {self.name}\nContact :{self.contact}\nCourse :{self.course}\nOffice_no :{self.office_no}"
class Ta(Student,Teacher):
    """This class is inheriting multiple classes at a time"""
    def __init__(self,name,contact,id):
        """The additional paramter will decide whether the ta will be a student or a teacher or both :)"""
        self.id=id
        if self.id==0:
            dep=input("ENter the department of the student :")
            sem=int(input("Enter the semseter of the student  :"))
            Student.__init__(self,name,contact,dep,sem)
        elif self.id==1:
             course=input("Enter the course of the Teacher :")
             office_no=int(input("Enter the office_no of the Teacher :"))
             Teacher.__init__(self,name,contact,course,office_no)
        else:
            dep = input("ENter the department of the student :")
            sem = int(input("Enter the semseter of the student  :"))
            course = input("Enter the course of the Teacher :")
            office_no = int(input("Enter the office_no of the Teacher :"))
            Student.__init__(self, name, contact, dep, sem)
            Teacher.__init__(self, name, contact, course, office_no)
    def __str__(self):
        if self.id==0:
            return f"Name :{self.name}\nContact :{self.contact}\nDep: {self.department}\nSemester :{self.semester}"
        elif self.id==1:
            return f"Name :{self.name}\nContact :{self.contact}\nCourse: {self.course}\nOffice_no :{self.office_no}"
        else:
            return f"Name :{self.name}\nContact :{self.contact}\nCourse: {self.course}\nOffice_no :{self.office_no}\nDepartment :{self.department}\nSemester :{self.semester}"
def main():
    p=Person("hammad farooq","01930910391")
    print(p)
    s=Student("Naeem Ullah","0103103091","data science",2)
    print(s)
    t=Teacher("Dr. iDress","0193091039","object oriented programming",3)
    print(t)
    ta=Ta("Hammad farooq","0130103",1)
    print(ta)
main()