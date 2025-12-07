class Student:
    def __init__ (self,roll_no,name,department,semseter,lasst_semseter_marks,ph_no):
        self.roll_no=roll_no.lower().ljust(12)
        self.name=name.ljust(31)
        self.department_code=department.ljust(3)
        self.semester=semseter
        self.last_semester_marks=lasst_semseter_marks
        self.phone_no=ph_no.ljust(12)
    @property
    def semester(self):
        return self._semester
    @semester.setter
    def semester (self,value):
        if type(value)==int:
            if value >=0:
                self._semester=value
            else:
                self.semester = int(input("Semseter can't be negative enter again :"))
        else:
            self.semester=int(input("Semseter can't be a string or flaot enter again :"))
    @property
    def last_semester_marks (self):
        return self._last_semester_marks
    @last_semester_marks.setter
    def last_semester_marks (self,value):
        if type(value)==float:
            self._last_semester_marks=value
        else:
            self.last_semester_marks=float(input("Enter the percentage again can't be a string or a integer :"))
if __name__=="__main__":###This method prevents the user from executing the code writeen after the class,WHEN IMPORTED AS A MODULE IN ANOTHER FILE
    s=Student("bsdsf22a026","Hammad farooq","ds",3.3,3,"01210310031")
# else:##when imported as a module the else part runs,when this file is executed the if blocks runs
#     ##it can also be tatken as a security measure __name__=="__main__"(environmental variables).
#     print("nono")

