class Polymomial():
    def __init__(self,list):
        self.degree=int(input("Enter the degree of your polymomial: "))
        self.degree1=self.degree
        self.degree2 = self.degree
        self.var=input("Enter the variable you want your polymonial in x or y? :")
        self.list=list
        self.polynomial=""
        self.new1 = ""
        self.new2=""
        self.new3=""
    @property
    def var(self):
        return self._var
    @var.setter
    def var(self,value):
        if value=="x" or value=="y":
            self._var=value
        else:
            self.var = input("Invalid Enter the variable you want your polymonial in x or y? :")


    def show(self):
        index = len(self.list) - 1
        for i in range(len(self.list),0,-1):
            self.element=self.list[i-1]
            if self.element>0:
                if self.element==self.list[index]:
                    self.polynomial += f"{self.element}{self.var}{self.degree}"
                else:
                    self.sign="+"
                    self.polynomial += f"{self.sign}{self.element}{self.var}{self.degree}"
            else:
                self.polynomial += f"{self.element}{self.var}{self.degree}"
            self.degree-=1
        for i in range(self.degree+1):##This will not run in case if list has more elements and degree is less because self.degree becomes zero
            self.sign = "+"
            if self.degree==0:
                self.polynomial += f"{self.sign}0"
            else:
                self.polynomial += f"{self.sign}0{self.var}{self.degree}"
                self.degree -= 1
    def __str__(self):
        return self.polynomial
    def __add__(self,other):
        if self.degree2>other.degree2:
            self.check2 = self.degree2
            difference = self.degree2 - other.degree2
            other3 = len(self.list) - difference
            index = len(self.list) - 1
            for i in range(len(self.list), other3, -1):
                self.element3 = self.list[i - 1]
                if self.element3 > 0:
                    if self.element3 == self.list[index]:
                        self.new3 += f"{self.element3}{self.var}{self.check2}"
                    else:
                        self.sign = "+"
                        self.new3 += f"{self.sign}{self.element3}{self.var}{self.check2}"
                else:
                    self.new3 += f"{self.element3}{self.var}{self.check2}"
                self.check2 -= 1
            for i in range(len(other.list), 0, -1):
                othar1 = 0
                if other3 > 0:
                    othar1 = self.list[other3 - 1]
                    other3 -= 1
                other.element3 = other.list[i - 1] + othar1
                if other.element3 > 0:
                    self.sign = "+"
                    self.new3 += f"{self.sign}{other.element3}{self.var}{self.check2}"
                else:
                    self.new3 += f"{other.element3}{self.var}{self.check2}"
                self.check2 -= 1
            self.new3 += f"{self.sign}0"
            return self.new3
        if self.degree2<other.degree2:
            self.check1 = other.degree2
            difference = other.degree2 - self.degree2
            other2=len(other.list)-difference
            index = len(other.list) - 1
            for i in range(len(other.list),other2,-1):
                self.element2 = other.list[i-1]
                if self.element2 > 0:
                    if self.element2 == other.list[index]:
                        self.new2 += f"{self.element2}{self.var}{self.check1}"
                    else:
                        self.sign = "+"
                        self.new2+= f"{self.sign}{self.element2}{self.var}{self.check1}"
                else:
                    self.new2 += f"{self.element2}{self.var}{self.check1}"
                self.check1 -= 1
            for i in range(len(self.list), 0, -1):
                othar = 0
                if other2>0:
                    othar=other.list[other2 - 1]
                    other2-=1
                self.element2 = self.list[i - 1]+othar
                if self.element2 > 0:
                    self.sign = "+"
                    self.new2+= f"{self.sign}{self.element2}{self.var}{self.check1}"
                else:
                    self.new2 += f"{self.element2}{self.var}{self.check1}"
                self.check1 -= 1
            self.new2 += f"{self.sign}0"
            return self.new2
        if self.degree1==other.degree1:
            self.check=self.degree1
            for i in range(len(self.list), 0, -1):
                self.element1 = self.list[i - 1]+other.list[i-1]
                index = len(self.list) - 1
                self.element = self.list[i - 1]
                if self.element1 > 0:
                    if self.element == self.list[index]:
                        self.new1 += f"{self.element1}{self.var}{self.check}"
                    else:
                        self.sign = "+"
                        self.new1+= f"{self.sign}{self.element1}{self.var}{self.check}"
                else:
                    self.new1 += f"{self.element1}{self.var}{self.check}"
                self.check -= 1
            return self.new1
p=Polymomial([1,9,-3,4])
p.show()
print(p)
q=Polymomial([5,4,-3,8,-12])
q.show()
print(q)
print(p+q)
