class Grades:
    def __init__ (self,course,roll_no,percentage_marks):
        self.course=course.ljust(21)
        self.roll_no=roll_no
        self.percentage_marks=percentage_marks