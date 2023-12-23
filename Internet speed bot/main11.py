class rational:
    def __init__(self):
        self.x=int(input("Enter the first number: "))
        self.y=int(input("Enter the second number: "))
        self.a = int(input("Enter the third number: "))
        self.b = int(input("Enter the fourth number: "))
        self.divide()
    def divide(self):
        self.x1=self.x/self.y
        self.a1=self.a/self.b
        self.mutiply()
    def mutiply(self):
        print(self.x1*self.a1)

r1=rational()
