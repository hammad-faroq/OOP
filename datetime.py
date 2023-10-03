class Datetime():
    def __init__(self,month,date,year):
        self.month=month
        self.date = date
        self.year=year
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self,value):
        if self.month == 2 and value > 28:
            self.date = int(input("Date for month 2 cannot exceed 28 Enter again :) :"))
        elif self.month==1 or self.month==3 or self.month==5 and value >31:
            self.date=int(input(f"Date for month {self.month} exceed 31 Enter again :) :"))
        elif self.month == 7 or self.month == 10 or self.month == 12 and value > 31:
            self.date = int(input(f"Date for month {self.month} exceed 31 Enter again :) :"))
        elif self.month==4 or self.month==6 or self.month==9  and value >30:
            self.date = int(input(f"Date for month {self.month} exceed 30 Enter again :) :"))
        elif self.month==11 and value>30:
            self.date = int(input(f"Date for month {self.month} exceed 30 Enter again :) :"))
        else:
            self._date=self.month
    @property
    def month(self):
        return self._month
    @month.setter
    def month(self,value):
        if value >12:
            self.month=int(input("Month cannot Exceed 12 Enter again :"))
        else:
            self._month=value
    @property
    def year(self):
        return self._year
    @year.setter
    def year(self,value):
        if value<0 and value<1000:
            self.year=int(input(F"Invalid year {value} Enter again :"))
        else:
            self._year=value

    def __str__(self):
        return f"{self._date}//{self.month}//{self.year}"
d=Datetime(2,33,2022)
print(f"{d.date)
print(d.month)
print(d.year)
