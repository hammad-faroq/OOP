
class Shapes:
    def __init__(self,canvas):
        self.canvas=canvas
        self.info_data = []
        self.more1 = [(0,0)]
        self.shape=input("Enter the shape you want to draw :")
        self.draw()

    @property
    def shape(self):
        return self._shape
    @shape.setter
    def shape(self,value):
        if value =="circle" or value=="square" or value=="rectangle" or value=="traingle" or value=="ellipse":
            self._shape=value
        else:
            self.shape=input("invalid input.Please check your spells.It must be written all small and enter again :")

    def draw(self):
        if self.shape == "circle":
            self.info="radius"
            self.circle()
        elif self.shape=="square":
            self.info="length and width"
            self.square()
        elif self.shape=="rectangle":
            self.info = "length and width"
            self.rectangle()
        elif self.shape=="traingle":
            self.info="length and height"
            self.traingle()
        elif self.shape=="ellipse":
            self.info="center and vertex"
            self.ellipse()


    def circle(self):
        self.data = input("Enter the radius of the circle :")
        self.check()
    def square(self):
        self.data=input("Enter the length and width of your sqaure in cm as a tuple :")
        self.check()
    def rectangle(self):
        self.data=input("Enter the length and width of your rectangle in cm as a tuple :")
        self.check()
    def traingle(self):
        self.data=input("Enter the length of base and height of the traingle in cm as a tuple :")
        self.check()
    def ellipse(self):
        self.data=input("Enter the center and vertex of ellipse in cm as a tuple :")
        self.check()
    def check(self):
        """This function is used to check if there is already a shape in that position or not ?"""
        self.x = int(input("Enter the x axis position :"))
        self.y=int(input("Enter the y axis postion :"))
        self.inside=input("Enter the inside colour of your shape :")
        self.colour = input("Enter the colour of the border :")
        self.info_data.append((self._shape,self.info,self.data,self.x,self.y,self.inside,self.colour))
    def more(self):
        """This is used to draw more shapes on the canvas"""
        self.shape = input("Enter the other shape you want to draw :")
        self.draw()
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self,value):
        for i in self.more1:
            if value==i[0]:
                self.x = int(input("There is already a shape at that point enter the x axis position again :"))
            else:
                self._x=value
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self,value):
        for i in self.more1:
            if value==i[1]:
                self.y = int(input("There is already a shape at that point enter the y axis position again :"))
        self.more1.append((self._x, value))
        self._y=value
    def all(self):
        """This method is used to print all the shapes on the canvas."""
        for i in self.info_data:
            print(f"A {i[0]} with {i[1]}cm ({i[2]}) and postion (x,y)={i[3],i[4]} with border color {i[5]} inside colour {i[6]}.")



    def __str__(self):
        """This is used to print only a single shape on the canvas"""
        return f"A {self._shape} with {self.info} ({self.data})cm and position (x,y)={self.x,self.y} with border colour {self.colour} and inside colour {self.inside}."

#________________________________________________This is the code of the canvas class_____________________________________________________________________#
#__________________________________________________________________________________________________________________________________________________________
class Canvas:
    def __init__(self,canvas):
        """This will take canvas as a tuple with length,width,colour as elements respectively"""
        self.canvas=canvas
        self.data()
    def data(self):
        self.length=self.canvas[0]
        self.width=self.canvas[1]
        self.canvas_colour=self.canvas[2]
        self.data1=f"A canvas with length {self.length} width {self.width} and bg {self.canvas_colour}."
    def __str__(self):
        return f"{self.data1}"

#________________________________________________This is the code of the canvas class_____________________________________________________________________#
#__________________________________________________________________________________________________________________________________________________________

def main():
    c=Canvas([300,300,"white"])
    s=Shapes(c)
    s.more()
    s.more()
    s.more()
    print(c)
    s.all()
main()


