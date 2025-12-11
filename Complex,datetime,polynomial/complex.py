class Complex:
    def __init__(self,i,y):
        self.i=i
        self.y=y
        if self.y>0:
            self.operation="+"
        else:
            self.operation="-"
    @property##we cacn make any public member private in getter and setter by using _ or __ (To make bot getters and setters tun in init)
    def operation(self):
        return self._operation
    @operation.setter#We use property decorators to automatically call the getters nad setters (when self.x)(getter callled)(when self.x=value)(setter called)(also to chech the invalid input by the end user)
    def operation(self,value):
            if value=="+" or value=="-":
                self._operation=value
            else:
                print("Invalid operation enter again",end="")
                self.operation = input(" Enter operation")
    def __str__(self):
        if self.y<0:
            return f"{self.i}i{self.y}"
        return f"{self.i}i{self.operation}{self.y}"
    def __add__(self,z):
        self.new=self.y+z.y
        if self.new>0:
            return f"{self.i+z.i}i{self.operation}{self.new}"
        return f"{self.i+z.i}i{self.new}"
    def __sub__(self, other):##Magic subtract function
        self.new1=self.y - other.y
        if self.new1>0:
            return f"{self.i-other.i}i{self.operation}{self.y-other.y}"
        return f"{self.i-other.i}i{self.y-other.y}"
    def __mul__(self, other):##magic function for multiplication
        self.new2=self.y*other.y
        if self.new2>0:
            return f"{self.i*other.i}i+{self.new2}"
        return f"{self.i*other.i}i{self.new2}"
    def __truediv__(self, other):##magic function for dividsion of \(float)
        self.new3=self.y/other.y
        if self.new3>0:
            return f"{self.i/other.i}i+{self.new3}"
        return f"{self.i / other.i}i{self.new3}"

c=Complex(-12,-5)
print(c)
z=Complex(12,30)
print(z)
print(c+z)
print()
print(c-z)
print(c*z)
print(z/c)