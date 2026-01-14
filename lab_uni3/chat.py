class Person(object):
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def __str__(self):
        return f"Name: {self.name}\nContact: {self.contact}"

class Student(Person):
    def __init__(self, name, contact, dep, sem):
        super().__init__(name, contact)
        self.department = dep
        self.semester = sem

    def __str__(self):
        return f"Name: {self.name}\nContact: {self.contact}\nDepartment: {self.department}\nSemester: {self.semester}"

class Teacher(Person):
    def __init__(self, name, contact, course, office_no):
        super().__init__(name, contact)
        self.course = course
        self.office_no = office_no

    def __str__(self):
        return f"Name: {self.name}\nContact: {self.contact}\nCourse: {self.course}\nOffice_no: {self.office_no}"

class Ta(Student, Teacher):
    def __init__(self, name, contact, dep, sem, course, office_no, id):
        # Call the __init__ method of Student using super()
        super(Student, self).__init__(name, contact, dep, sem)
        # Call the __init__ method of Teacher using super()
        Teacher.__init__(self,name, contact, course, office_no)
        self.id = id

    def __str__(self):
        return f"Name: {self.name}\nContact: {self.contact}\nDepartment: {self.department}\nSemester: {self.semester}\nCourse: {self.course}\nOffice_no: {self.office_no}\nID: {self.id}"

# Creating instances
ta = Ta("Ali hamza", "019309103", "adadad", 3, "oop", 5, 1)


def test_case(self):
    """THIS IS THE TEST CASE FOR THE MAGNITUDE OF THE VECTOR TO CHECK WHETHER THE VALUES ARE EQAUL OR NOT, BY USING BUILT-IN-FUNCTIONS AND SIMPLE CALCULATIONS"""
    mag = 0
    for i in self.tupe:
        mag += i ** 2
    mag = round(mag ** 0.5, 2)
    result = round(math.sqrt(sum(x ** 2 for x in self.tupe)), 2)
    if mag == result:
        print("Test case passed")
    else:
        print("test case failed!")

# Printing information
print(ta)

# class Person(object):
#     def __init__(self, name, contact):
#         self.name = name
#         self.contact = contact
#
#     def __str__(self):
#         return f"Name: {self.name}\nContact: {self.contact}"
#
# class Student(Person):
#     def __init__(self, name, contact, dep, sem):
#         super().__init__(name, contact)
#         self.department = dep
#         self.semester = sem
#
#     def __str__(self):
#         return f"Name: {self.name}\nContact: {self.contact}\nDepartment: {self.department}\nSemester: {self.semester}"
#
# class Teacher(Person):
#     def __init__(self, name, contact, course, office_no):
#         super().__init__(name, contact)
#         self.course = course
#         self.office_no = office_no
#
#     def __str__(self):
#         return f"Name: {self.name}\nContact: {self.contact}\nCourse: {self.course}\nOffice_no: {self.office_no}"
#
# class Ta(Student, Teacher):
#     def __init__(self, name, contact, dep, sem, course, office_no, id):
#         # Explicitly call the __init__ methods of Student and Teacher
#         Student.__init__(self, name, contact, dep, sem)
#         Teacher.__init__(self, name, contact, course, office_no)
#         self.id = id
#
#     def __str__(self):
#         return f"Name: {self.name}\nContact: {self.contact}\nDepartment: {self.department}\nSemester: {self.semester}\nCourse: {self.course}\nOffice_no: {self.office_no}\nID: {self.id}"
#
# # Creating instances
# ta = Ta("Ali hamza", "019309103", "adadad", 3, "oop", 5, 1)
#
# # Printing information
# print(ta)

# class Person(object):
#     def __init__(self, name, contact):
#         self.name = name
#         self.contact = contact
#
#     def __str__(self):
#         return f"Name: {self.name}\nContact: {self.contact}"
#
# class Student(Person):
#     def __init__(self, name, contact, dep, sem):
#         Person.__init__(self, name, contact)
#         self.department = dep
#         self.semester = sem
#
#     def __str__(self):
#         return f"Name: {self.name}\nContact: {self.contact}\nDepartment: {self.department}\nSemester: {self.semester}"
#
# class Teacher(Person):
#     def __init__(self, name, contact, course, office_no):
#         Person.__init__(self, name, contact)
#         self.course = course
#         self.office_no = office_no
#
#     def __str__(self):
#         return f"Name: {self.name}\nContact: {self.contact}\nCourse: {self.course}\nOffice_no: {self.office_no}"
#
# class Ta(Student, Teacher):
#     def __init__(self, name, contact, dep, sem, course, office_no, id):
#         # Call the __init__ method of Student and Teacher directly
#         Student.__init__(self, name, contact, dep, sem)
#         Teacher.__init__(self, name, contact, course, office_no)
#         self.id = id
#
#     def __str__(self):
#         return f"Name: {self.name}\nContact: {self.contact}\nDepartment: {self.department}\nSemester: {self.semester}\nCourse: {self.course}\nOffice_no: {self.office_no}\nID: {self.id}"
#
# p = Person("hammad farooq", "01930910391")
# print(p)
#
# s = Student("Naeem Ullah", "0103103091", "data science", 2)
# print(s)
#
# t = Teacher("Dr. iDress", "0193091039", "object-oriented programming", 3)
# print(t)
#
# ta = Ta("Ali hamza", "019309103", "adadad", 3, "oop", 5, 1)
# print(ta)
